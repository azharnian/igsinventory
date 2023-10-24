from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.locations.buildings import *
from application.resources.locations.buildings import *

buildings = Blueprint('buildings', __name__)