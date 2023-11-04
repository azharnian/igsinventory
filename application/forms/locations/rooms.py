from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddRoomForm(FlaskForm):
    room_code = StringField('Room Code', validators=[DataRequired(), Length(max=256)])
    room_name = StringField('Room Name', validators=[DataRequired(), Length(max=256)])
    floor_id = IntegerField('Floor ID', validators=[DataRequired()])
    note = StringField('Note', validators=[Length(max=256)])
    active = BooleanField('Active', default=True)
    submit = SubmitField('Add Room')

class UpdateRoomForm(AddRoomForm):
    submit = SubmitField('Update Room')
