from flask import Blueprint, render_template

docs = Blueprint('docs', __name__)

@docs.route("/", methods=["GET"])
@docs.route("/docs", methods=["GET"])
def index():
    return render_template("index.html")