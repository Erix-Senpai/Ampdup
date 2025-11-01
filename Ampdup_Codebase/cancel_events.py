from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import CancelEventForm


cancel_event_bp = Blueprint('CancelEvent', __name__, url_prefix='/CancelEvent')

@cancel_event_bp.route('/<event_id>', methods=['POST', 'GET'])
@login_required
def cancel_event(event_id):
    if not current_user.is_authenticated:
        flash('Please log in to cancel ticket')
        return redirect(url_for('auth.login'))
    
    cancel_event_form = CancelEventForm()
    if cancel_event_form.validate_on_submit():
        if not (event_id):
            flash('Event not found.')
            return redirect(url_for('main.index'))
        
        event = db.session.get(Event, event_id)    #Query for event submitted.
        if (event.owner_id != current_user.id):
            flash('Warning: Owner validation failed!')
            return redirect(url_for('main.index'))
        if not (event):
            flash('Event not found.')
            return redirect(url_for('main.index'))
        
        
        #Update event status. No further action is taken.
        event.status = "Cancelled"
        event.statusCode = "badge2"
        db.session.commit()

        flash(f" Event cancellation for event {event.title} with evend id {event_id} has \nSuccessfully cancelled.")
        return redirect(url_for('BookingHistory.Get_Booking'))



 