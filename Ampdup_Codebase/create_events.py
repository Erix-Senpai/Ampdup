from flask import Blueprint, render_template, url_for, redirect, flash
from .forms import EventForm
from .models import upload_event
from flask_login import login_required, current_user
from . import db
from Ampdup_Codebase import db
from .models import Event

create_event_bp = Blueprint('CreateEvent', __name__, url_prefix="/Create_Event")

# Event Routing Bp, dedicated for returning event details.
@create_event_bp.route('/', methods=['GET', 'POST'])
@login_required
def Create_Event():
    event_form = EventForm()    #Call for form EventForm()
    if (event_form.validate_on_submit()):   #If Submitted Form is valid.
        upload_event(event_form)    #Upload_Event into database.
        return redirect(url_for('BookingHistory.Get_Booking'))     # Redirect to bookingHistory page, where they shiould see their event created.
    
    # Loads the page of Create Event.
    return render_template('CreateEvent.html', event_form=event_form, active_page='Create Event')


@create_event_bp.route('/update/<int:event_id>', methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    event = db.session.get(Event, event_id)

    if not event:
        flash('Event not found.')
        return redirect(url_for('main.index'))

    if event.owner_id != current_user.id:
        flash('You do not have permission to edit this event.')
        return redirect(url_for('event.event_details', id=event.id))

    form = EventForm(obj=event)  # prefill with existing event data

    if form.validate_on_submit():
        form.populate_obj(event)  # update event fields directly
        db.session.commit()
        flash(f'Event "{event.title}" was successfully updated!')
        return redirect(url_for('event.event_details', id=event.id))

    return render_template('update_event.html', event_form=form, event=event)
