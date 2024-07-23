from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# This is the route for the home page
@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")

# This is the route for the about page
@views.route('/profile')
def profile():
    return render_template("profile.html")



