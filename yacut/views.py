from random import sample
import string

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import CutURLForm
from .models import URLMap


def get_unique_short_id() -> str:
    """Рекурсивный генератор короткой ссылки"""

    symbols = string.ascii_letters + string.digits
    short_id = ''.join(sample(symbols, 6))
    if URLMap.query.filter_by(short=short_id).first() is not None:
        get_unique_short_id()
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if custom_id is None or custom_id == '':
            custom_id = get_unique_short_id()

        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('main.html', form=form)

        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id
        )

        db.session.add(url_map)
        db.session.commit()
        context = {'form': form, 'short_id': url_map.short}
        return render_template('main.html', **context)

    return render_template('main.html', form=form)


@app.route('/<path:short_id>')
def redirect_to_original_view(short_id):
    short_link = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(short_link.original)
