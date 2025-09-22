from flask import Blueprint, flash, render_template, request, url_for, redirect
from .forms import EventForm
event_bp = Blueprint('CreateEvent', __name__)

# Event Routing Bp, dedicated for returning event details.
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
        ### Tell SQLAlchemy to save the above data + the StatusCode.
        match EventStatus:
            # Status Code is stored as a variable, returns as the code to identify the colour code for the status into html.
            case "Open": StatusCode = "badge1"
            case "Sold Out": StatusCode = "badge2"
            case "Cancelled": StatusCode = "badge3"
            case "Inactive": StatusCode = "badge4"
            case _ : StatusCode = "badge4"
        # return to booking history page, where user should see their own events as well as other past events.
        return redirect(url_for('main.BookingHistory'))
    
    # Loads the page of Create Event.
    return render_template('CreateEvent.html', event_form=event_form)
