from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/eventdetails')
def eventdetails():
    return render_template('Event Details.html')

@mainbp.route('/bookinghistory')
def bookinghistory():
    return render_template('BookingHistory.html')

@mainbp.route('/createevent')
def createevent():
    return render_template('CreateEvent.html')