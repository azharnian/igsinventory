from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.utils import *
from application.forms.locations.rooms import *
from application.resources.locations.rooms import *

rooms = Blueprint('rooms', __name__)

@rooms.route('/rooms')
@login_required
def all():
    rooms = get_all_rooms()
    data = []
    for room in rooms:
        data.append({
            'ID': room.id,
            'Room Name': room.room_name,
            'Action': f'<div class="action-btn"><a href="{url_for('rooms.update', id=room.id)}">📝</a>'
        })#<a style="margin-left: 15px;" href="{url_for('rooms.delete', id=room.id)}">❌</a></div>
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table-bordered', escape=False, index=False)

    return render_template('pages/rooms/view_all_rooms.html', title="All Rooms", html_table=html_table)

@rooms.route('/rooms/update')
@rooms.route('/rooms/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    room_data = get_room_by_id(id)
    if not id or not room_data:
        return redirect(url_for('rooms.all'))
    form = UpdateRoomForm()
    floors = Floor.query.all()
    form.floor_id.choices = [(floor.id, floor.name) for floor in floors]

    if form.validate_on_submit():
        room_data = {
            'note': form.note.data,
            'active': form.active.data,
            'room_code': form.room_code.data,
            'room_name': form.room_name.data,
            'floor_id': form.floor_id.data,
        }
        res = update_room(id, room_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('rooms.all'))
        flash('Update failed', 'danger')

    form.note.data = room_data.note
    form.active.data = room_data.active
    form.room_code.data = room_data.room_code
    form.room_name.data = room_data.room_name
    form.floor_id.data = room_data.floor_id

    return render_template('pages/rooms/update_room.html', title=f"Update Room: {room_data.room_name}", form=form)

@rooms.route('/rooms/delete/<int:id>')
def delete(id=0):
    if not id:
        return redirect(url_for('rooms.all'))
    res = delete_room(id)
    if res:
        flash('Delete success.', 'success')
    else:
        flash('Something wrong.', 'danger')
    return redirect(url_for('rooms.all'))

@rooms.route('/rooms/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddRoomForm()

    floors = Floor.query.all()
    form.floor_id.choices = [(floor.id, floor.name) for floor in floors]

    if form.validate_on_submit():
        room_data = {
            'note': form.note.data,
            'active': form.active.data,
            'room_code': form.room_code.data,
            'room_name': form.room_name.data,
            'floor_id': form.floor_id.data,
            'created_by': current_user.id
        }

        res = create_room(room_data)
        if res:
            flash('Add room successful.', 'success')
            return redirect(url_for('rooms.all'))
        flash('Something wrong', 'error')

    return render_template('pages/rooms/add_room.html', title='Add Room', form=form)
