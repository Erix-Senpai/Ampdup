from flask import Blueprint, request, render_template, redirect, url_for
from .models import Event, Comment
from .forms import CommentForm

eventsbp = Blueprint('event', __name__, url_prefix='/events')

from Ampdup_Codebase import db

@eventsbp.route('/<id>', methods=['GET', 'POST'])
def event_details(id):
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    form = CommentForm()          # Create the form instance
    
    if form.validate_on_submit():
        print(f"The following comment has been posted: {form.text.data}")  # Handles POST submission
        new_comment = Comment(
            user="Anonymous",
            text=form.text.data,
            created_at="2025-09-18 19:00:00"
        )
        event.set_comments(new_comment)
        return redirect(url_for('event.event_details', event=event, form=form))

    # Pass the form to the template
    return render_template('Event_Details.html', event=event, form=form)

# def get_event():
#     b_desc = """Previously titled the 'After Hours Tour', this is the seventh concert tour by Canadian singer-songwriter
#                 The Weeknd. The Weeknd is bringing the 'After Hours Til Dawn Tour' to Brisbane's Suncorp Stadium."""
#     image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
#     event = Event('The Weeknd: After Hours Til Dawn Tour', b_desc, image_loc, 'R$10')

#     # Add some dummy comments
#     event.set_comments(Comment("John Doe", "I'm so excited for this! I can't wait.", '2023-08-12 11:00:00'))
#     event.set_comments(Comment("Devashree Kadia", "The goat finally coming to Brisbane omg.", '2023-08-12 11:00:00'))
#     event.set_comments(Comment("Sally", "Free face masks!", '2023-08-12 11:00:00'))
#     event.set_comments(Comment("Test", "Example", '2023-08-12 11:00:00'))

#     return event
