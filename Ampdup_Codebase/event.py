from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm
event_bp = Blueprint('CreateEvent', __name__)

@event_bp.route('/CreateEvent', methods=['GET', 'POST'])
def Event():
    event_form = EventForm()
    if (event_form.validate_on_submit()):
        EventTitle = event_form.EventTitle.data
        EventDescription = event_form.EventDescription.data
        EventImage = event_form.EventImage.data
        EventDate = event_form.EventDate.data
        EventStartTime = event_form.EventStartTime.data
        EventEndTime = event_form.EventEndTime.data
        EventLocation = event_form.EventLocation.data
        EventType = event_form.EventType.data
        EventStatus = event_form.EventStatus.data
        print("DEBUG - Got Event:")
        return redirect(url_for('main.BookingHistory'))
    
    
    return render_template('CreateEvent.html', event_form=event_form)
