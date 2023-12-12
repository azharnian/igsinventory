from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, DateTimeField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    length = FloatField('Length', default=0)
    width = FloatField('Width', default=0)
    height = FloatField('Height', default=0)
    weight = FloatField('Weight', default=0)
    color = StringField('Color')
    photo_item = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    is_electronic = BooleanField('Is Electronic', default=False)
    is_waterresistant = BooleanField('Is Water Resistant', default=False)
    price = FloatField('Price', default=0)
    make = StringField('Make')
    model = StringField('Model')
    store = StringField('Store')
    volume_cc = FloatField('Volume CC', default=0)
    material = StringField('Material')
    machine_number = StringField('Machine Number')
    police_state_number = StringField('Police State Number')
    serial_number = StringField('Serial Number')
    date_purchased = DateTimeField('Date Purchased', format='%Y-%m-%d', validators=[Optional()], default=datetime.utcnow())
    budget_type = StringField('Budget Type')
    origin_country = StringField('Origin Country')
    percent_depreciation_per_year = FloatField('Percent Depreciation Per Year', default=0)
    percent_demage = FloatField('Percent Damage', default=0)
    is_available = BooleanField('Is Available', default=True)
    is_broken = BooleanField('Is Broken', default=False)
    is_active = BooleanField('Is Active', default=True)
    photo_location = StringField('Photo Location')
    room_id = SelectField('Room ID', validators=[DataRequired()])
    item_type_id = SelectField('Item Type ID', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Item')

class UpdateItemForm(AddItemForm):
    code = StringField('Code', validators=[DataRequired()])
    submit = SubmitField('Update Item')
