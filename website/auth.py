from flask import Blueprint, render_template
# This is the blueprint for the auth of the website
auth = Blueprint('auth', __name__)
# This is the route for the login page
@auth.route('/login')
def login():
    return render_template("login.html")

# This is the route for the sign up page
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

# This is the route for the logout page
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# This is the route for the profile page
@auth.route('/profile')
def profile():
    return "<p>Profile</p>"

# This is the route for the reset password page
@auth.route('/reset-password')
def reset_password():
    return "<p>Reset Password</p>"
