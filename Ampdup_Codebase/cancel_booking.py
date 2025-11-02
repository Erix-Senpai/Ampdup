from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import CancelBookingForm


cancel_booking_bp = Blueprint('CancelBooking', __name__, url_prefix='/Cancel_Booking')


@cancel_booking_bp.route('/<booking_id>', methods=['POST', 'GET'])
@login_required
def cancel_booking(booking_id):
    if not current_user.is_authenticated:
        flash('Please log in to cancel ticket')
        return redirect(url_for('auth.login'))
    #Cancel booking form action.
    cancel_form = CancelBookingForm()
    if cancel_form.validate_on_submit():
        
        if (not booking_id or booking_id == 'none'):
            flash('Booking not found.')
            return redirect(url_for('main.index'))
        
        booked_event = Booking.query.filter_by(id = booking_id, user_id = current_user.id).first()  #Query for Bookings of current user.

        if not booked_event:
            flash('Booking not found.')
            return redirect(url_for('main.index'))
        
        if (booked_event.user_id != current_user.id):
            flash('Warning: Booking user validation failed!')
            return redirect(url_for('main.index'))
        
        event = db.session.get(Event, booked_event.event_id)    #Query for events that were booked.

        if not event:
            flash('Event not found.')
            return redirect(url_for('main.index'))
        
        ticket_quantity = int(booked_event.quantity)    #Update ticket remaining for the event, and update db.
        event.ticket_remain += ticket_quantity
        db.session.delete(booked_event)
        db.session.commit()
    
        flash(f" Booking cancellation for event {event.title} with booking id {booking_id} has \nSuccessfully cancelled.")
        return redirect(url_for('BookingHistory.Get_Booking'))



 