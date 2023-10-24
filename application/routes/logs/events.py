from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.logs.events import *
from application.resources.logs.events import *

events = Blueprint('events', __name__)