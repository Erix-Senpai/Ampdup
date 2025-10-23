from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm
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
    your_event_ = Event.query.filter_by(owner_id=current_user.id).all()
    your_event = []
    for event in your_event_:
        image = event.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        your_event__ = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "image": image,
            "price": event.price,
            "date": event.date,
            "startTime": event.startTime,
            "endTime": event.endTime,
            "location": event.location,
            "type": event.type,
            "status": event.status,
            "statusCode": event.statusCode,
            "owner_id": event.owner_id
        }
        your_event.append(your_event__)
    booked_event_ = Event.query.join(Booking, Booking.event_id == Event.id).filter(Booking.user_id == current_user.id).all()
    booked_event = []
    for event in booked_event_:
        image = event.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        booked_event__ = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "image": image,
            "price": event.price,
            "date": event.date,
            "startTime": event.startTime,
            "endTime": event.endTime,
            "location": event.location,
            "type": event.type,
            "status": event.status,
            "statusCode": event.statusCode,
            "owner_id": event.owner_id
        }
        booked_event.append(booked_event__)
    return render_template('BookingHistory.html', booked_event=booked_event, your_event=your_event, active_page='Get_History')
