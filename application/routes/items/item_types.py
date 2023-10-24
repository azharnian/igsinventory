from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint

from application.utils import *
from application.forms.items.item_types import *
from application.resources.items.item_types import *

item_types = Blueprint('item_types', __name__)