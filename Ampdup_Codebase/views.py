from flask import Blueprint, render_template, request, redirect, url_for
from .index_database import Populate_Event

# Registration
from .models import User, Booking, Comment, Event
from .forms import RegisterForm, CommentForm
from Ampdup_Codebase import db

mainbp = Blueprint('main', __name__ , template_folder='../templates')



@mainbp.route('/')
def index():
    events = Populate_Event()
    return render_template('index.html', events = events, active_page='Home')



@mainbp.route('/BookingHistory')
def BookingHistory():
    return render_template('BookingHistory.html', active_page='Check Booking')



@mainbp.route('/Event_Details')
def Event_Details():
    return render_template('Event_Details.html')



@mainbp.route('/<id>/comment',methods=["GET","POST"])
def comment(id):
    print('Method type: ', request.method)
    form = CommentForm()
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    if form.validate_on_submit():

        c   = Comment(  text  = form.text.data,
                        event = event)
        
        db.session.add(c)
        db.session.commit()
        
        print('Successful Comment Post')
        return redirect(url_for('main.index'))
    return render_template('register/register.html',form=form)


