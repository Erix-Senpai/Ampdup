from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import CancelBookingForm, CancelEventForm
from datetime import datetime


cancel_booking_bp = Blueprint('CancelBooking', __name__, url_prefix='/Cancel_Booking')


@cancel_booking_bp.route('/cancel_booking', methods=['POST', 'GET'])
def cancel_booking(booking_id):
    event_id = request.args.get('event_id', 'none')
    booking_id = request.args.get('booking_id', 'none')
    if not current_user.is_authenticated:
        flash('Please log in to cancel ticket')
        return redirect(url_for('auth.login'))  
    cancel_form = CancelBookingForm()
    if cancel_form.validate_on_submit():
        booked_event = Booking.query.filter_by(id = booking_id, user_id = current_user.id).first()
        event = db.session.get(Event, booked_event.event_id)

        if not event:
            flash('Event not found.')
            return redirect(url_for('main.index'))
        if not booked_event:
            flash('Booking not found.')
            return redirect(url_for('main.index'))
        
        ticket_quantity = int(booked_event.quantity)
        event.ticket_remain += ticket_quantity
        db.session.delete(booked_event)
        db.session.commit()
        flash(f" Booking cancellation for event {event.title} with booking id {booking_id} has \nSuccessfully cancelled.")

    cancel_event_form = CancelEventForm()
    if cancel_event_form.validate_on_submit():
        event = db.session.get(Event, id = event_id)
        if not event:
            flash('Event not found.')
            return redirect(url_for('main.index'))
        event.status = "Cancelled"
        event.statusCode = "badge2"
        db.session.commit()

        flash(f" Booking cancellation for event {event.title} with evend id {event_id} has \nSuccessfully cancelled.")
        return redirect(url_for('BookingHistory.Get_Booking'))



 