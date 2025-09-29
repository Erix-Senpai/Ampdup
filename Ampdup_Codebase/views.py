from flask import Blueprint, render_template, request, redirect, url_for
from .index_database import Populate_Event
mainbp = Blueprint('main', __name__ , template_folder='../templates')

@mainbp.route('/')
def index():
    events = Populate_Event()
    print(events)
    return render_template('index.html', events = events, active_page='Home')

@mainbp.route('/BookingHistory')
def BookingHistory():
    return render_template('BookingHistory.html', active_page='Check Booking')

@mainbp.route('/Event_Details')
def Event_Details():
    return render_template('Event_Details.html')


from .models import User
from .forms import RegisterForm
from Ampdup_Codebase import db

@mainbp.route('/register',methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        p = User(user_name=form.user_name.data, email=form.email.data, password=form.password.data)
        db.session.add(p)
        db.session.commit()
        print('Successful User Registration')
        return redirect(url_for('index.html'))
    return redirect(url_for('index.html'))
