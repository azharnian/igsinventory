from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class AddFloorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=256)])
    description = TextAreaField('Description')
    building_id = SelectField('Building ID', validators=[DataRequired()])
    photo_location = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Floor')

class UpdateFloorForm(AddFloorForm):
    submit = SubmitField('Update Floor')
