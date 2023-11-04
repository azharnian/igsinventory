import qrcode
from PIL import Image
from io import BytesIO
import base64

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