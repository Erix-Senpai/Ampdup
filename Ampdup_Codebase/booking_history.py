from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import CancelBookingForm, CancelEventForm
from . import db
from .models import Event, Booking
from flask_login import login_required, current_user
from .return_query import return_booking_event_query, return_event_query
booking_history_bp = Blueprint('BookingHistory', __name__, url_prefix="/Booking_History")

# Event Routing Bp, dedicated for returning booking history.
@booking_history_bp.route('/', methods=['GET', 'POST'])
# Class that returns booking histories.
@login_required
def Get_Booking():
    cancelBookingForm = CancelBookingForm()
    cancelEventForm = CancelEventForm()

    
    your_event_query = Event.query.filter_by(owner_id=current_user.id).all()    #Query for all your_event
    your_event = return_event_query(your_event_query)   #Turn list of event objects into dicts, allowing flexibility.
    

    booked_event_query = (db.session.query(Booking, Event).join(Event, Booking.event_id == Event.id).filter(Booking.user_id == current_user.id).all())  #Query for all booked_event
    booked_event = return_booking_event_query(booked_event_query)   #Turn tuple into dicts, allowing flexibility.

    return render_template('BookingHistory.html', booked_event=booked_event, cancelBookingForm = cancelBookingForm, cancelEventForm = cancelEventForm, your_event=your_event, active_page='Get_History', view_mode = 'past_booking')

