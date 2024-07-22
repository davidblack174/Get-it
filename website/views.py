from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# This is the route for the home page
@views.route('/')
def home():
    return render_template("home.html")
