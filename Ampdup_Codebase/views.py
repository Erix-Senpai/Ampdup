from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__ , template_folder='../templates')

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/BookingHistory')
def BookingHistory():
    return render_template('BookingHistory.html')

@mainbp.route('/CreateEvent')
def CreateEvent():
    return render_template('CreateEvent.html')
