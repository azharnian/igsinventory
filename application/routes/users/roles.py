from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.users.roles import *
from application.resources.users.roles import *

roles = Blueprint('roles', __name__)