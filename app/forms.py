from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from app import mongo

class URLForm(FlaskForm):
    url = StringField('url', 
                      validators=[DataRequired()], 
                      render_kw={"placeholder": "url"})
    alias = StringField('alias', 
                        validators=[DataRequired(), Length(min=4)], 
                        render_kw={"placeholder": "alias"})
    submit = SubmitField('Submit')