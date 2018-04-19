from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from app import mongo

class URLForm(FlaskForm):
    url = StringField('url', 
                      validators=[DataRequired()], 
                      render_kw={"placeholder": "url"})
    submit = SubmitField('Submit')