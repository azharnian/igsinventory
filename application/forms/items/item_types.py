from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class AddItemTypeForm(FlaskForm):
    name_type = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Item Type')

class UpdateItemTypeForm(AddItemTypeForm):
    submit = SubmitField('Update Item Type')
