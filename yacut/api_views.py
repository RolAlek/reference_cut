from collections import OrderedDict
import re

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_link():
    """Создание короткой ссылки."""
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    custom_id = data.get('custom_id')
    if custom_id is None or custom_id == '':
        custom_id = get_unique_short_id()

    if custom_id and not re.match('^[a-zA-Z0-9]+$', custom_id) or len(custom_id) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')

    link = URLMap(original=data.get('url'), short=custom_id)
    db.session.add(link)
    db.session.commit()

    short_link = url_for('redirect_to_original_view', short_id=link.short, _external=True)
    response_data = OrderedDict([('url', link.original), ('short_link', short_link)])
    return jsonify(response_data), 201


@app.route('/api/id/<path:short_id>/', methods=['GET'])
def get_original_link(short_id):
    """Получение ориганальной ссылкой по короткому идентификатору."""
    short_link = URLMap.query.filter_by(short=short_id).first()
    if short_link is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(short_link.to_dict()), 200