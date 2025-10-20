from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
#from .models import User
from .forms import LoginForm, RegisterForm
#from . import db
from flask import session

# Create a blueprint - make sure all BPs have unique names
auth_bp = Blueprint('auth', __name__)

# this is a hint for a login function
@auth_bp.route('/login', methods=['GET', 'POST'])

# view function

def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():  
        email = loginForm.email.data
        password_hash = loginForm.password_hash.data
        session['user_name'] = loginForm.email.data
        print('Successfully logged in')
        flash('You logged in successfully')
        return redirect(url_for('main.index'))
    return render_template('user.html', form=loginForm,  heading='Login')

@auth_bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Successfully registered')
        return redirect(url_for('main.index'))
    return render_template('user.html', form=form)

@auth_bp.route('/logout')
def logout():
    if 'user_name' in session:
        session.pop('user_name')
    flash('You have been logged out')
    print('Successfully logged out')
    return redirect(url_for('main.index'))

