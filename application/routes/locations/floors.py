from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.utils import *
from application.forms.locations.floors import *
from application.resources.locations.floors import *

floors = Blueprint('floors', __name__)

@floors.route('/floors')
@login_required
def all():
    floors = get_all_floors()
    data = []
    for floor in floors:
        data.append({
            'Id': floor.id,
            'Name': floor.name,
            'Building ID': floor.building_id,
            'Description': floor.description,
            'Action': f'<div class="action-btn"><a href="{url_for('floors.update', id=floor.id)}">📝</a><a style="margin-left: 15px;" href="{url_for('floors.delete', id=floor.id)}">❌</a></div>'
        })
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table-bordered', escape=False, index=False)

    return render_template('pages/floors/view_all_floors.html', title="All Floors", html_table=html_table)

@floors.route('/floors/update')
@floors.route('/floors/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    floor_data = get_floor_by_id(id)
    if not id or not floor_data:
        return redirect(url_for('floors.all'))
    form = UpdateFloorForm()

    if form.validate_on_submit():
        floor_data = {
            'name': form.name.data,
            'building_id': form.building_id.data,
            'description': form.description.data,
            'photo_location': form.photo_location.data,
        }
        res = update_floor(id, floor_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('floors.all'))
        flash('Update failed', 'danger')

    form.name.data = floor_data.name
    form.building_id.data = floor_data.building_id
    form.description.data = floor_data.description
    form.photo_location.data = floor_data.photo_location

    return render_template('pages/floors/update_floor.html', title=f"Update Floor: {floor_data.name}", form=form)

@floors.route('/floors/delete/<int:id>')
def delete(id=0):
    if not id:
        return redirect(url_for('floors.all'))
    res = delete_floor(id)
    if res:
        flash('Delete success.', 'success')
    else:
        flash('Something wrong.', 'danger')
    return redirect(url_for('floors.all'))

@floors.route('/floors/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddFloorForm()

    if form.validate_on_submit():
        floor_data = {
            'name': form.name.data,
            'building_id': form.building_id.data,
            'description': form.description.data,
            'photo_location': form.photo_location.data,
            'created_by': current_user.id
        }

        res = create_floor(floor_data)
        if res:
            flash('Add floor successful.', 'success')
            return redirect(url_for('floors.all'))
        flash('Something wrong', 'error')

    return render_template('pages/floors/add_floor.html', title='Add Floor', form=form)
