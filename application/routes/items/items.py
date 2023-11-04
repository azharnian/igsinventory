from flask import render_template, redirect, url_for, flash, request
from flask import Blueprint
from flask_login import login_required, current_user

from datetime import datetime
import pandas as pd

from application.models.items.items import *
from application.models.items.item_types import *
from application.forms.items.items import *
from application.resources.items.items import *
from application.utils import generate_qr_code

items = Blueprint('items', __name__)

@items.route('/items')
@login_required
def all():
    items = Item.query.all()
    data = []
    for item in items:
        data.append({
            'ID': item.id,
            'Code': item.code,
            'Name': item.name,
            'Action': f'<div class="action-btn"><a href="{url_for("items.update", id=item.id)}">📝</a><a style="margin-left: 15px;" href="{url_for("items.delete", id=item.id)}">❌</a></div>'
        })
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table-bordered', escape=False, index=False)

    return render_template('pages/items/view_all_items.html', title="All Items", html_table=html_table)

@items.route('/items/update', methods=['GET', 'POST'])
@items.route('/items/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    item = Item.query.get(id)
    if not id or not item:
        return redirect(url_for('items.all'))

    qrcode = generate_qr_code(item.code)
    form = UpdateItemForm(obj=item)

    if form.validate_on_submit():
        item_data = {
            'code': form.code.data,
            'name': form.name.data,
            'length': form.length.data,
            'width': form.width.data,
            'height': form.height.data,
            'weight': form.weight.data,
            'color': form.color.data,
            'photo_item': form.photo_item.data,
            'is_electronic': form.is_electronic.data,
            'is_waterresistant': form.is_waterresistant.data,
            'price': form.price.data,
            'make': form.make.data,
            'model': form.model.data,
            'store': form.store.data,
            'volume_cc': form.volume_cc.data,
            'material': form.material.data,
            'machine_number': form.machine_number.data,
            'police_state_number': form.police_state_number.data,
            'serial_number': form.serial_number.data,
            'date_purchased': form.date_purchased.data,
            'budget_type': form.budget_type.data,
            'origin_country': form.origin_country.data,
            'percent_depreciation_per_year': form.percent_depreciation_per_year.data,
            'percent_demage': form.percent_demage.data,
            'is_available': form.is_available.data,
            'is_broken': form.is_broken.data,
            'is_active': form.is_active.data,
            'photo_location': form.photo_location.data,
            'room_id': form.room_id.data,
            'item_type_id': form.item_type_id.data,
            'description': form.description.data
        }
        res = update_item(id, item_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('items.all'))

    return render_template('pages/items/update_item.html', title=f'Update Item: {item.name}', qrcode=qrcode.decode('utf-8'), form=form)

@items.route('/items/delete/<int:id>')
@login_required
def delete(id=0):
    item = Item.query.get(id)
    if not id or not item:
        return redirect(url_for('items.all'))

    delete_item(item.id)
    flash('Delete success.', 'success')
    return redirect(url_for('items.all'))

@items.route('/items/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddItemForm()
    rooms = Room.query.all()
    item_types = ItemType.query.all()
    form.room_id.choices = [(room.id, room.room_name) for room in rooms]
    form.item_type_id.choices = [(item_type.id, item_type.name_type) for item_type in item_types]

    if form.validate_on_submit():
        item_data = form.data
        item_data['date_created'] = datetime.utcnow()
        item_data['created_by'] = current_user.id
        create_item(item_data)
        flash('Add item successful.', 'success')
        return redirect(url_for('items.all'))

    return render_template('pages/items/add_item.html', title='Add Item', form=form)


@items.route('/items/scan', methods=['GET', 'POST'])
@login_required
def scan():

    return render_template('pages/items/scan_item.html', title='Scan Item')