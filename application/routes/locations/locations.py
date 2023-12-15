from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.utils import *
from application.forms.locations.locations import *
from application.resources.locations.locations import *

locations = Blueprint('locations', __name__)

@locations.route('/locations')
@login_required
def all():
    locations = get_all_locations()
    data = []
    for location in locations:
        data.append({
            'Id': location.id,
            'Name': location.name,
            'Long': location.longitude,
            'Lat': location.latitude,
            'Action' : f'<div class="action-btn"><a href="{url_for("locations.update", id=location.id)}">📝</a>'
        })#<a style="margin-left: 15px;" href="{url_for('locations.delete', id=location.id)}">❌</a></div>
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table table-bordered', escape=False, index=False)

    return render_template('pages/locations/view_all_locations.html', title="All Locations", html_table=html_table)

@locations.route('/locations/update')
@locations.route('/locations/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    loc_data = get_location_by_id(id)
    if not id or not loc_data:
        return redirect(url_for('locations.all'))
    form = UpdateLocationForm()

    if form.validate_on_submit():
        loc_data = {
            'name' :  form.name.data,
            'longitude' : form.longitude.data,
            'latitude' : form.latitude.data,
            'description' : form.description.data,
            'photo_location' : form.photo_location.data
        }
        res = update_location(id, loc_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('locations.all'))
        flash('Update failed', 'danger')

    form.name.data = loc_data.name
    form.longitude.data = loc_data.longitude
    form.latitude.data = loc_data.latitude
    form.description.data = loc_data.description

    return render_template('pages/locations/update_location.html', title=f"Update Location : {loc_data.name}", form=form)

@locations.route('/locations/delete/<int:id>')
def delete(id=0):
    if not id:
        return redirect(url_for('locations.all'))
    res = delete_location(id)
    if res:
        flash('Delete success.', 'success')
    else:   
        flash('Something wrong.', 'danger')
    return redirect(url_for('locations.all'))

@locations.route('/locations/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddLocationForm()

    if form.validate_on_submit():
        loc_data = {
            'name' :  form.name.data,
            'longitude' : form.longitude.data,
            'latitude' : form.latitude.data,
            'description' : form.description.data,
            'photo_location' : form.photo_location.data,
            'created_by' : current_user.id
        }

        res = create_location(loc_data)
        if res:
            flash('Add location successful.', 'success')
            return redirect(url_for('locations.all'))
        flash('Something wrong', 'error')

    return render_template('pages/locations/add_location.html', title='Add Location', form=form)
