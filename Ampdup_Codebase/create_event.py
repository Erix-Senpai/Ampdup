from flask import Blueprint, flash, render_template, request, url_for, redirect
create_event_bp = Blueprint('Create_Event', __name__)

@create_event_bp.route('/Create_Event', methods=['POST'])
def Create_Event():
    EventTitle = request.form.get("CreateEventTitle")
    EventDescription = request.form.get("CreateEventDescription")
    EventImage = request.form.get("CreateEventImage")
    EventStartTime = request.form.get("CreateEventStartTime")
    EventEndTime = request.form.get("CreateEventEndTime")
    EventLocation = request.form.get("CreateEventLocation")
    EventType = request.form.get("CreateEventType")
    EventStatus = request.form.get("CreateEventStatus")
    print("DEBUG - Got Event:", EventTitle, EventDescription, EventImage)
    return redirect(url_for('main.index'))
