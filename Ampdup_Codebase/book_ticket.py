from flask import Blueprint, flash, render_template, request, url_for, redirect
book_ticket_bp = Blueprint('book_ticket', __name__)

@book_ticket_bp.route('/book_ticket', methods=['POST'])
def Ticket():
    EventTitle = request.form.get("CreateEventTitle")
    EventDescription = request.form.get("CreateEventDescription")
    EventImage = request.form.get("CreateEventImage")
    EventStartTime = request.form.get("CreateEventStartTime")
    EventEndTime = request.form.get("CreateEventEndTime")
    EventLocation = request.form.get("CreateEventLocation")
    EventType = request.form.get("CreateEventType")
    EventStatus = request.form.get("CreateEventStatus")
    print("DEBUG - Got Event:", EventTitle, EventDescription, EventImage)
    return redirect(url_for('main.BookingHistory'))
