import os
import qrcode
from PIL import Image
from io import BytesIO
import base64
import secrets

from flask import current_app
from wtforms.validators import ValidationError

from application import db, login_manager
from application.models.users.users import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if user:
        raise ValidationError("Email already exists. Please use a different email.")
    
def not_exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if not user:
        raise ValidationError("Email not found.")

def exists_username(form, username):
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username")

def save_picture(form_picture, prefix):
    random_hex = secrets.token_hex(5)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f'assets/images/{prefix}/'+random_hex+f_ext
    picture_path = os.path.join(current_app.root_path, 'static/', picture_fn)
    
    basewidth = 500
    image = Image.open(form_picture)
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    image = image.resize((basewidth, hsize))

    image.save(picture_path)

    return picture_fn

def generate_qr_code(code):
    qr_url = qrcode.make(str(code))
    qr_img = BytesIO()
    qr_url.save(qr_img, "PNG")
    encoded_qr_img = base64.b64encode(qr_img.getvalue())
    return encoded_qr_img

def generate_qr_code_with_logo(code, logo_path):

    basewidth = 50
    logo = Image.open(logo_path)
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(code))
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    logo_position = ((qr_img.width - logo.width) // 2, (qr_img.height - logo.height) // 2)

    qr_img.paste(logo, logo_position)

    qr_output = BytesIO()
    qr_img.save(qr_output, "PNG")
    encoded_qr_img = base64.b64encode(qr_output.getvalue())
    return encoded_qr_img