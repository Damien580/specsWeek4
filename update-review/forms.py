from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class DinosaurForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    herbivore = BooleanField('is herbivore?', default=False)
    submit = SubmitField("submit")