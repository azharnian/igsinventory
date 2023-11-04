from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

import pandas as pd

from application.forms.items.item_types import *
from application.models.items.item_types import *
from application.resources.items.item_types import *

item_types = Blueprint('item_types', __name__)

@item_types.route('/item_types')
@login_required
def all():
    item_types = ItemType.query.all()
    data = []
    for item_type in item_types:
        data.append({
            'ID': item_type.id,
            'Name Type': item_type.name_type,
            'Description': item_type.description,
            'Date Created': item_type.date_created,
            'Date Updated': item_type.date_updated,
            'Action': f'<div class="action-btn"><a href="{url_for("item_types.update", id=item_type.id)}">📝</a><a style="margin-left: 15px;" href="{url_for("item_types.delete", id=item_type.id)}">❌</a></div>'
        })
    df = pd.DataFrame(data)
    html_table = df.to_html(classes='table table-striped table-bordered', escape=False, index=False)

    return render_template('pages/item_types/view_all_item_types.html', title="All Item Types", html_table=html_table)

class AddItemTypeForm(FlaskForm):
    name_type = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Item Type')

@item_types.route('/item_types/update')
@item_types.route('/item_types/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    item_type = ItemType.query.get(id)
    if not id or not item_type:
        return redirect(url_for('item_types.all'))

    form = UpdateItemTypeForm()

    if form.validate_on_submit():
        item_type_data = {
            'name_type': form.name_type.data,
            'description': form.description.data,
        }
        res = update_item_type(id, item_type_data)
        if res:
            flash('Update success.', 'success')
            return redirect(url_for('rooms.all'))
        flash('Update failed', 'danger')

    form.name_type.data = item_type.name_type
    form.description.data = item_type.description

    return render_template('pages/item_types/update_item_types.html', title=f'Update Item Type: {item_type.name_type}', form=form)

@item_types.route('/item_types/delete/<int:id>')
@login_required
def delete(id=0):
    item_type = ItemType.query.get(id)
    if not id or not item_type:
        return redirect(url_for('item_types.all'))
    
    delete_item_type(id)
    flash('Delete success.', 'success')
    return redirect(url_for('item_types.all'))

@item_types.route('/item_types/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddItemTypeForm()

    if form.validate_on_submit():
        item_type_data = {
            'name_type': form.name_type.data,
            'description': form.description.data,
            'created_by' : current_user.id
        }

        res = create_item_type(item_type_data)
        if res:
            flash('Add item type successful.', 'success')
            return redirect(url_for('item_types.all'))
        flash('Something wrong', 'error')

    return render_template('pages/item_types/add_item_types.html', title='Add Item Type', form=form)
