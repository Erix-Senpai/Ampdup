from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm
from .models import upload_event
from . import db
from .models import Event
from flask_login import login_required
from sqlalchemy import Column, Integer, String, Text, Float, LargeBinary
booking_history_bp = Blueprint('BookingHistory', __name__, url_prefix="/Booking_History")

# Event Routing Bp, dedicated for returning event details.
@booking_history_bp.route('/', methods=['GET', 'POST'])
@login_required
def Get_Booking():
    event = db.session.scalar(db.select(Event).where(Event.owner_id==id))
    return event