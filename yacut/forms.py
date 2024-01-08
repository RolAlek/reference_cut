from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from . import MAX_LENGTH_SHORT_ID, PATTERN


class CutURLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired('Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                max=MAX_LENGTH_SHORT_ID,
                message='Превышение допустимой длинны 16 символов'
            ),
            Regexp(
                regex=PATTERN,
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
