from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.logs.logs import *
from application.resources.logs.logs import *

logs = Blueprint('logs', __name__)