from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from app import mongo

class URLForm(FlaskForm):
    inURL = StringField('url to shorten', validators=[DataRequired()])
    outURL = StringField('new url suffix', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Submit')