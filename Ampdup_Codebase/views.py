from flask import Blueprint, render_template
from .index_database import Populate_Event
mainbp = Blueprint('main', __name__ , template_folder='../templates')

@mainbp.route('/')
def index():
    events = Populate_Event()
    return render_template('index.html', events = events, active_page='Home')

@mainbp.route('/BookingHistory')
def BookingHistory():
    return render_template('BookingHistory.html', active_page='Check Booking')

@mainbp.route('/Event_Details')
def Event_Details():
    return render_template('Event_Details.html')
