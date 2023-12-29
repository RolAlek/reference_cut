from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class CutURLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired('Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16, 'Превышение допустимой длинны 16 символов'),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
