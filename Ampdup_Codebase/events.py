from flask import Blueprint, request, render_template, redirect, url_for
from .models import Comment
from .event_db import Event
from .forms import CommentForm
from . import db

eventsbp = Blueprint('event', __name__, url_prefix='/events')


@eventsbp.route('/<id>', methods=['GET', 'POST'])
def event_details(id):
    event = db.session.scalar(db.select(Event).where(Event.eventUid==id))           # Get the dummy event
    form = CommentForm()          # Create the form instance
    
    if form.validate_on_submit():
        # read the comment from the form, associate the Comment's event field
        # with the event object from the above DB query
        comment = Comment(text=form.text.data, event=event) 
        # here the back-referencing works - comment.event is set
        # and the link is created
        db.session.add(comment) 
        db.session.commit() 
        # flashing a message which needs to be handled by the html
        # flash('Your comment has been added', 'success')  
        print('Your comment has been added', 'success') 
        # using redirect sends a GET request to event.show
        return redirect(url_for('event.event_details', id=id))

    # Pass the form to the template
    return render_template('Event_Details.html', event=event, form=form)

def get_event():
    event_desc = """Previously titled the 'After Hours Tour', this is the seventh concert tour by Canadian singer-songwriter
                The Weeknd. The Weeknd is bringing the 'After Hours Til Dawn Tour' to Brisbane's Suncorp Stadium."""
    image_loc = url_for('static', filename='img folder/the weeknd.jpg')
    event_loc = 'Suncorp Stadium, 40 Castlemaine St, Milton QLD 4064'
    event_dt = 'Sat, 18 October, 6:00pm - 8:30pm AEST'
    event = Event('The Weeknd: After Hours Til Dawn Tour', event_desc, image_loc, 'From $50', event_loc, event_dt)

    # Add some dummy comments
    event.set_comments(Comment("John Doe", "I'm so excited for this! I can't wait.", '2023-08-12 11:00:00'))
    event.set_comments(Comment("Devashree Kadia", "The goat finally coming to Brisbane omg.", '2023-08-12 11:00:00'))
    event.set_comments(Comment("Sally", "Free face masks!", '2023-08-12 11:00:00'))

    return event
