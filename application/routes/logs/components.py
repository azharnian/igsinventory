from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.logs.components import *
from application.resources.logs.components import *

components = Blueprint('components', __name__)