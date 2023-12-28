from random import sample
import string

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import CutURLForm
from .models import URLMap


def get_unique_short_id() -> str:
    """Рекурсиный генератор короткой ссылки"""
    symbols = string.ascii_letters + string.digits
    short_id = ''.join(sample(symbols, 6))
    if URLMap.query.filter_by(short=short_id).first() is not None:
        return get_unique_short_id()
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first() is not None and custom_id != '':
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('main.html', form=form)

        short_id = URLMap(
            original=form.original_link.data,
            short=custom_id if custom_id != '' else get_unique_short_id()
        )

        db.session.add(short_id)
        db.session.commit()
        context = {'form': form, 'short_id': short_id}
        return render_template('main.html', **context)

    return render_template('main.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        abort(404)
    return redirect(url.original)
