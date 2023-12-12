from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileField, FileAllowed

class AddBuildingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=256)])
    address = StringField('Address', validators=[DataRequired(), Length(max=256)])
    location_id = SelectField('Location ID', validators=[DataRequired()])
    rt = StringField('RT', default="00")
    rw = StringField('RW', default="00")
    kelurahan = StringField('Kelurahan', validators=[DataRequired(), Length(max=256)])
    kecamatan = StringField('Kecamatan', validators=[DataRequired(), Length(max=256)])
    city = StringField('City', validators=[DataRequired(), Length(max=256)])
    province = StringField('Province', validators=[DataRequired(), Length(max=256)])
    zip_code = StringField('ZIP Code', validators=[Optional(), Length(max=6)])
    photo_location = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    description = TextAreaField('Description')
    submit = SubmitField('Add Building')

class UpdateBuildingForm(AddBuildingForm):
    submit = SubmitField('Update Building')
