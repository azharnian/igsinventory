from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.activities.updates import *
from application.resources.activities.updates import *

updates = Blueprint('updates', __name__)