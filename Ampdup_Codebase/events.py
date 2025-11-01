from flask import Blueprint, request, render_template, redirect, url_for, flash
from .models import Event, Comment
from .forms import CommentForm, PurchaseForm, CancelBookingForm, CancelEventForm
from datetime import date, datetime, time
from .return_query import return_single_event_query

# Get the current datetime object

from flask_login import current_user
from . import db
import base64
from Ampdup_Codebase import db

eventsbp = Blueprint('event', __name__, url_prefix='/events')
@eventsbp.route('/<id>', methods=['GET', 'POST'])
def event_details(id):
    view_mode = request.args.get('view_mode', 'default')
    form = CommentForm()   
    purchaseform = PurchaseForm()       # Create purchase form instance
    cancelBookingForm = CancelBookingForm()     #Create cancel booking form instance
    cancelEventForm = CancelEventForm()     #Create cancel event form instance

    query = db.session.scalar(db.select(Event).where(Event.id==id))
    event = return_single_event_query(query)

    # Check for the dates upon loading events by updating the status.
    end_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
    end_time = datetime.strptime(event["endTime"], "%H:%M:%S").time()
    # If event is Not Cancelled, and the date is past the event date, update event status to Inactive.
    if (end_date < date.today() and end_time < datetime.now().time() and event.status != 'Cancelled'):

        event.status = 'Inactive'
        event.statusCode = 'badge4'          
        db.session.commit()
            # change active status"
    # Comment form
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Please log in to make a comment')
            return redirect(url_for('auth.login'))  # Redirect to login if not authenticated
        # read the comment from the form, associate the Comment's event field
        # with the event object from the above DB query
        comment = Comment(text=form.text.data, event=event, user=current_user) 
        # here the back-referencing works - comment.event is set
        # and the link is created
        db.session.add(comment) 
        db.session.commit() 
        # flashing a message which needs to be handled by the html
        # flash('Your comment has been added', 'success')  
        print('Your comment has been added', 'success') 
        # using redirect sends a GET request to event.show
        return redirect(url_for('event.event_details', event = event, event_id=id, view_mode = view_mode))

    # Pass the form to the template
    return render_template('Event_Details.html', event=event, form=form, purchaseform = purchaseform, cancelBookingForm = cancelBookingForm, cancelEventForm = cancelEventForm, view_mode = view_mode)
