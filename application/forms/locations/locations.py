from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileField, FileAllowed

class AddLocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=256)])
    longitude = FloatField('Longitude', validators=[Optional()])
    latitude = FloatField('Latitude', validators=[Optional()])
    description = TextAreaField('Description')
    photo_location = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Location')

class UpdateLocationForm(AddLocationForm):
    submit = SubmitField('Update Location')
