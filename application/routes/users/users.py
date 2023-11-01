from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint
from flask_login import current_user, login_required, login_user, logout_user

from application.utils import *
from application.forms.users.users import *
from application.resources.users.users import *

users = Blueprint('users', __name__)

#SESSION
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)
        if user and user.password == form.password.data:
            login_user(user)
            next_url = request.args.get('next') or url_for('users.index')
            return redirect(next_url)
        flash('Something wrong, please try again', 'danger')
    return render_template('pages/users/login.html', title='Login', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        user_data = {
            'username': form.username.data,
            'email': form.email.data,
            'phone': form.phone.data,
            'password': form.password.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'role': 0
        }
        
        res = create_user(user_data)
        if res:
            flash('Registration successful.', 'success')
            return redirect(url_for('users.login'))
        flash('Something wrong', 'error')

    return render_template('pages/users/register.html', title='Register', form=form)

#USER_PAGE

#dasboard
@users.route('/')
@login_required
def index():
    return render_template("index.html", title='Dashboard')

@users.route('/profile')
@login_required
def profile():
    pass

@users.route('/forgot', methods=['GET', 'POST'])
def forgot():
    pass

@users.route('/reset', methods=['GET', 'POST'])
@login_required
def reset():
    pass


#ADMIN_PAGE
@users.route('/logs', methods=['GET', 'POST'])
@login_required
def logs():
    pass

@users.route('/confirm', methods=['GET', 'POST'])
@login_required
def confirm():
    pass

@users.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    pass

@users.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    pass

@users.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    pass