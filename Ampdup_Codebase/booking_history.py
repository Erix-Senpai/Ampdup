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
booking_history_bp = Blueprint('BookingHistory', __name__, url_prefix="/Booking_History")

# Event Routing Bp, dedicated for returning event details.
@booking_history_bp.route('/', methods=['GET', 'POST'])
@login_required
def Get_Booking():
    cancelBookingForm = CancelBookingForm()

    your_event_query = (db.session.query(Booking, Event).join(Event, Booking.event_id == Event.id).filter(Event.owner_id == current_user.id).all())
    your_event = return_event_query(your_event_query)
    

    booked_event_query = (db.session.query(Booking, Event).join(Event, Booking.event_id == Event.id).filter(Booking.user_id == current_user.id).all())
    booked_event = return_event_query(booked_event_query)

    return render_template('BookingHistory.html', booked_event=booked_event, cancelBookingForm = cancelBookingForm, your_event=your_event, active_page='Get_History', view_mode = 'past_booking')




def return_event_query(query: Query):
    event_list = []
    for bookings, events in query:
        image = events.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        e_list = {
            "booking_id": bookings.id,
            "event_id": events.id,
            "quantity": bookings.quantity,
            "order_date": bookings.order_date,
            "title": events.title,
            "description": events.description,
            "image": image,
            "price": events.price,
            "date": events.date,
            "startTime": events.startTime,
            "endTime": events.endTime,
            "location": events.location,
            "type": events.type,
            "status": events.status,
            "statusCode": events.statusCode,
            "owner_id": events.owner_id
        }
        event_list.append(e_list)

    return event_list

