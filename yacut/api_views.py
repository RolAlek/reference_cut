from flask import jsonify

from . import app
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_link():
    #TODO: допили api для создания короткой ссылки
    ...


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    #TODO: допили api-метод для получения ссылки по короткому идентификатору
    ...