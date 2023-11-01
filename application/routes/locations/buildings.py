from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.utils import *
from application.forms.locations.buildings import *
from application.resources.locations.buildings import *

buildings = Blueprint('buildings', __name__)

@buildings.route('/buildings')
@login_required
def all():
    buildings = get_all_buildings()
    data = []
    for building in buildings:
        data.append({
            'Id': building.id,
            'Name': building.name,
            'Address': building.address,
            'Location ID': building.location_id,
            'Kelurahan': building.kelurahan,
            'Kecamatan': building.kecamatan,
            'City': building.city,
            'Action' : f'<div class="action-btn"><a href="{url_for('buildings.update', id=building.id)}">📝</a><a style="margin-left: 15px;" href="{url_for('buildings.delete', id=building.id)}">❌</a></div>'
        })
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table table-bordered', escape=False, index=False)

    return render_template('pages/buildings/view_all_buildings.html', title="All Buildings", html_table=html_table)

@buildings.route('/buildings/update')
@buildings.route('/buildings/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    building_data = get_building_by_id(id)
    if not id or not building_data:
        return redirect(url_for('buildings.all'))
    form = UpdateBuildingForm()

    if form.validate_on_submit():
        building_data = {
            'name': form.name.data,
            'address': form.address.data,
            'location_id': form.location_id.data,
            'rt': form.rt.data,
            'rw': form.rw.data,
            'kelurahan': form.kelurahan.data,
            'kecamatan': form.kecamatan.data,
            'city': form.city.data,
            'province': form.province.data,
            'zip_code': form.zip_code.data,
            'photo_location': form.photo_location.data,
            'description': form.description.data,
        }
        res = update_building(id, building_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('buildings.all'))
        flash('Update failed', 'danger')

    form.name.data = building_data.name
    form.address.data = building_data.address
    form.location_id.data = building_data.location_id
    form.rt.data = building_data.rt
    form.rw.data = building_data.rw
    form.kelurahan.data = building_data.kelurahan
    form.kecamatan.data = building_data.kecamatan
    form.city.data = building_data.city
    form.province.data = building_data.province
    form.zip_code.data = building_data.zip_code
    form.photo_location.data = building_data.photo_location
    form.description.data = building_data.description

    return render_template('pages/buildings/update_building.html', title=f"Update Building: {building_data.name}", form=form)

@buildings.route('/buildings/delete/<int:id>')
def delete(id=0):
    if not id:
        return redirect(url_for('buildings.all'))
    res = delete_building(id)
    if res:
        flash('Delete success.', 'success')
    else:
        flash('Something wrong.', 'danger')
    return redirect(url_for('buildings.all'))

@buildings.route('/buildings/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddBuildingForm()

    if form.validate_on_submit():
        building_data = {
            'name': form.name.data,
            'address': form.address.data,
            'location_id': form.location_id.data,
            'rt': form.rt.data,
            'rw': form.rw.data,
            'kelurahan': form.kelurahan.data,
            'kecamatan': form.kecamatan.data,
            'city': form.city.data,
            'province': form.province.data,
            'zip_code': form.zip_code.data,
            'photo_location': form.photo_location.data,
            'description': form.description.data,
            'created_by': current_user.id
        }

        res = create_building(building_data)
        if res:
            flash('Add building successful.', 'success')
            return redirect(url_for('buildings.all'))
        flash('Something wrong', 'error')

    return render_template('pages/buildings/add_building.html', title='Add Building', form=form)
