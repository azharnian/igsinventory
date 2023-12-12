import qrcode
from PIL import Image
from io import BytesIO
import base64

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