from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.locations.locations import *
from application.resources.locations.locations import *

locations = Blueprint('locations', __name__)