from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm, CancelBookingForm
from sqlalchemy.orm import Query
from .models import upload_event
from . import db
import base64
from .models import Event
from .models import Booking
from flask_login import login_required, current_user
from sqlalchemy import Column, Integer, String, Text, Float, LargeBinary
from .return_query import return_booking_event_query, return_event_query
booking_history_bp = Blueprint('BookingHistory', __name__, url_prefix="/Booking_History")

# Event Routing Bp, dedicated for returning event details.
@booking_history_bp.route('/', methods=['GET', 'POST'])
@login_required
def Get_Booking():
    cancelBookingForm = CancelBookingForm()

    your_event_query = Event.query.filter_by(owner_id=current_user.id).all()
    your_event = return_event_query(your_event_query)
    print(f"YOUR BOOKING: {your_event.__len__()}")
    

    booked_event_query = (db.session.query(Booking, Event).join(Event, Booking.event_id == Event.id).filter(Booking.user_id == current_user.id).all())
    booked_event = return_booking_event_query(booked_event_query)

    return render_template('BookingHistory.html', booked_event=booked_event, cancelBookingForm = cancelBookingForm, your_event=your_event, active_page='Get_History', view_mode = 'past_booking')

