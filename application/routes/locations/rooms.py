from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.locations.rooms import *
from application.resources.locations.rooms import *

rooms = Blueprint('rooms', __name__)