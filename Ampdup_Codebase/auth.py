from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from .forms import LoginForm, RegisterForm
from . import db
from flask import session

# Create a blueprint - make sure all BPs have unique names
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])

# view function
def login():
    loginform = LoginForm()
    error = None
    if loginform.validate_on_submit():
        email = loginform.email.data
        password = loginform.password.data
        user = db.session.scalar(db.select(User).where(User.email==email))
        if user is None:
            error = 'This email is not registered. Please register first.'
        elif not check_password_hash(user.password_hash, password): # takes the hash and cleartext password
            error = 'Incorrect password'
        if error is None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=loginform,  heading='Login')



@auth_bp.route('/register', methods = ['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        flash('Successfully registered')
        first_name = registerform.first_name.data
        surname = registerform.surname.data
        email = registerform.email.data
        phone_number = registerform.phone_number.data
        street_address = registerform.street_address.data
        password = registerform.password.data
        
        # create a hashed password
        password_hash = generate_password_hash(password)
        
        #create a new user model object
        new_user = User(
            first_name = first_name,
            surname = surname,
            email = email,
            phone_number = phone_number,
            street_address = street_address,
            password_hash = password_hash
        )
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered! Please log in.')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=registerform, heading='Register')



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

