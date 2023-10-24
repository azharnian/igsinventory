from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.items.items import *
from application.resources.items.items import *

items = Blueprint('items', __name__)