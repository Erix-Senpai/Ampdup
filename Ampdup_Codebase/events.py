from flask import Blueprint, request, render_template, redirect, url_for, flash
from .models import Event, Comment
from .forms import CommentForm, PurchaseForm, Cancellation_form
from datetime import date, datetime

# Get the current datetime object

from flask_login import current_user
from . import db
import base64

eventsbp = Blueprint('event', __name__, url_prefix='/events')

from Ampdup_Codebase import db
@eventsbp.route('/<id>', methods=['GET', 'POST'])
def event_details(id):
    view_mode = request.args.get('view_mode', 'default') # Get view mode from query parameters, default to 'default'
    event = db.session.scalar(db.select(Event).where(Event.id==id)) # Query the event by ID
    form = CommentForm()   # Create comment form
    purchaseform = PurchaseForm()       # Create purchase form
    cancellation_form = Cancellation_form() #create cancellation form
    image = event.image #get image from database
    encoded_image = base64.b64encode(image).decode("utf-8") #encode image to base64
    image = f"data:image/png;base64,{encoded_image}" #prepare image for display

    due_date = datetime.strptime(event.date, "%Y-%m-%d").date() #convert string to date object
    end_time = datetime.strptime(event.endTime, "%H:%M:%S").time() #convert string to time object
    if (due_date < date.today() and end_time < datetime.now().time() and event.status != 'Cancelled'): #check if event date has passed to change status to inactive

        event.status = 'Inactive'
        event.statusCode = 'badge4'          
        db.session.commit()
            # change active status"
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
        return redirect(url_for('event.event_details', id=id, view_mode = view_mode))

    # Pass the form to the template
    return render_template('Event_Details.html', event=event, form=form, purchaseform = purchaseform, cancellation_form = cancellation_form, image = image, view_mode = view_mode)
