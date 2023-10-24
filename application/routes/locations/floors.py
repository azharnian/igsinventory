from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.locations.floors import *
from application.resources.locations.floors import *

floors = Blueprint('floors', __name__)