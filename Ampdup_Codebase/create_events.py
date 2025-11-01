from flask import Blueprint, render_template, url_for, redirect
from .forms import EventForm
from .models import upload_event
from flask_login import login_required
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
