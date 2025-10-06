from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm
from .models import upload_event
create_event_bp = Blueprint('CreateEvent', __name__, url_prefix="/Create_Event")

# Event Routing Bp, dedicated for returning event details.
@create_event_bp.route('/', methods=['GET', 'POST'])
def Create_Event():
    event_form = EventForm()
    if (event_form.validate_on_submit()):
        upload_event(event_form)
        return redirect(url_for('main.BookingHistory'))
    
    # Loads the page of Create Event.
    return render_template('CreateEvent.html', event_form=event_form, active_page='Create Event')
