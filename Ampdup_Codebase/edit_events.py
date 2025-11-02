from flask import Blueprint, render_template, url_for, redirect, flash, request
from .forms import EventForm
from flask_login import current_user, login_required
from .models import Event
from . import db
from datetime import datetime

edit_event_bp = Blueprint('EditEvent', __name__, url_prefix="/Edit_Event")

# Event Routing Bp, dedicated for returning event details.
@edit_event_bp.route('/<event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):

    event = db.session.get(Event, event_id)  #Query for event submitted.
    # Convert DB objects for datetime from str to datetime.
    if (event.owner_id != current_user.id):     #Safecheck if owner == current user.
        flash('Warning: Owner validation failed!')
        return redirect(url_for('main.index'))

    event_form = EventForm()
    if (event_form.validate_on_submit()):   #If Submitted Form is valid.
        update_event(event, event_form)
        # commit to the database
        db.session.commit()
        flash("Event updated successfully!")
        return redirect(url_for('BookingHistory.Get_Booking'))
    
    # Loads the page of Create Event.
    if request.method == "GET":
        event.date = datetime.strptime(event.date, "%Y-%m-%d").date()
        event.startTime = datetime.strptime(event.startTime, "%H:%M:%S").time()
        event.endTime = datetime.strptime(event.endTime, "%H:%M:%S").time()
        event_form = EventForm(obj=event)

    return render_template('EditEvent.html', event_form = event_form, event_id=event_id, view_mode = 'past_booking')

def update_event(event, event_form):
    event.title = event_form.title.data
    event.description = event_form.description.data
    if event_form.image.data:
        event.image = event_form.image.data.read()
    event.price = event_form.price.data
    event.ticket = event_form.ticket.data
    event.ticket_remain = event.ticket
    date = event_form.date.data
    event.date = str(date)
    startTime = event_form.startTime.data
    event.startTime = str(startTime)
    endTime = event_form.endTime.data
    event.endTime = str(endTime)
    event.location = event_form.location.data
    event.type = event_form.type.data
    event.status = "Open"
    event.statusCode = "badge1"
    event.owner_id = current_user.id