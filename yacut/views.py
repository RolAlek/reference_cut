from random import sample

from flask import flash, redirect, render_template

from . import app, db, LENGTH_SHORT_ID, SYMBOLS
from .forms import CutURLForm
from .models import URLMap


def get_unique_short_id() -> str:
    """Генератор короткой ссылки"""
    while True:
        short_id = ''.join(sample(SYMBOLS, LENGTH_SHORT_ID))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if not custom_id or custom_id == '':
            custom_id = get_unique_short_id()

        if URLMap.query.filter_by(short=custom_id).first():
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
