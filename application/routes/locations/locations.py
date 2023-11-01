from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.utils import *
from application.forms.locations.locations import *
from application.resources.locations.locations import *

locations = Blueprint('locations', __name__)

@locations.route('/locations/view_all_locations')
# @login_required
def view_all_locations():
    locations = get_all_locations()
    data = []
    for location in locations:
        data.append({
            'Name': location.name,
            'Longitude': location.longitude,
            'Latitude': location.latitude,
            'Description': location.description,
            'Date Created': location.date_created,
            'Date Updated': location.date_updated,
            'Photo Location': location.photo_location
        })
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table table-bordered text-center', escape=False, index=False)

    return render_template('pages/locations/view_all_locations.html', title="All Locations", html_table=html_table)

@locations.route('/locations/add', methods=['GET', 'POST'])
@login_required
def add_location():
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
        else:
            flash('Something wrong', 'error')

    return render_template('pages/locations/add_location.html', title='Add Location', form=form)