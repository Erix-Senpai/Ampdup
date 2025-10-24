from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import Cancellation_form
from datetime import datetime


cancel_booking_bp = Blueprint('CancelBooking', __name__)


@cancel_booking_bp.route('/<int:event_id>', methods=['POST', 'GET'])
def cancel_booking(event_id):
    if not current_user.is_authenticated:
        flash('Please log in to cancel ticket')
        return redirect(url_for('auth.login'))  

    else:
        event = db.session.get(Event, event_id)
        if not event:
            flash('Event not found.')
            return redirect(url_for('main.index'))
        cancel_form = Cancellation_form()
        if cancel_form.validate_on_submit():
            booked_event = Booking.query.filter_by(user_id=current_user.id, event_id=event.id)
            print(f"BOOKED EVENT: {booked_event}")
            print(f"CURRENT USER ID:{current_user.id}")
            print(f"CURRENT EVENT ID: {event.id}")
            ticket_quantity = int(booked_event.quantity)
            event.ticket_remain += ticket_quantity
            db.session.delete(booked_event)
        db.session.commit()
        flash(f" Booking cancellation for event {event.title} \nSuccessfully cancelled.")
        return redirect(url_for('BookingHistory.Get_Booking'))



 