from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__ , template_folder='../templates')

@mainbp.route('/')
def index():
    return render_template('index.html', active_page='Home')

@mainbp.route('/BookingHistory')
def BookingHistory():
    return render_template('BookingHistory.html', active_page='Check Booking')

@mainbp.route('/CreateEvent')
def CreateEvent():
    return render_template('CreateEvent.html', active_page='Create Event')
print("hello")

@mainbp.route('/Event_Details')
def Event_Details():
    return render_template('Event_Details.html')