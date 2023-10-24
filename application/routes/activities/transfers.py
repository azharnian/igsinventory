from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.activities.transfers import *
from application.resources.activities.transfers import *

transfers = Blueprint('transfers', __name__)