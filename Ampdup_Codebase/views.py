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
        
        db.session.add(c) # add comment to session
        db.session.commit() # write to database
        
        print('Successful Comment Post')
        return redirect(url_for('main.index'))
    return render_template('register/register.html',form=form)


@mainbp.route('/trigger500') #Creat a route to trigger a 500 error
def trigger500():
    # Force a runtime error
    1 / 0
    return "You’ll never see this"


import base64
import sqlalchemy
from sqlalchemy import desc, asc

#--Search Route
@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        events = db.session.scalars( db.select(Event).where( (Event.title.like(query)) + (Event.description.like(query)) ) ) 
        
        newevents = list()
        for event in events:
            image = event.image
            encoded_image = base64.b64encode(image).decode("utf-8")
            image = f"data:image/png;base64,{encoded_image}"
            event.image = image
            newevents.append(event)
            
        if (newevents.__len__() > 0):
            return render_template('searchresults.html', events=newevents)
        else:   
            return render_template('nosearchresults.html')
        
    else:
        return redirect(url_for('main.index'))
    
  
  
#--Sort Route
@mainbp.route('/sort')
def sort():
    if request.args['sort'] and request.args['sort'] != "":
        if "id_asc" in request.args['sort']:
            #   Ascending ID
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(asc(Event.id)) ) 
            
        elif 'id_desc' in request.args['sort']:
            #   Descending ID
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(desc(Event.id))  )
            
        elif 'name_asc' in request.args['sort']:
            #   Ascending Title
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(asc(Event.title))  )
            
        elif 'name_desc' in request.args['sort']:
            #   Descending Title
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(desc(Event.title))  )
            
        elif 'date_asc' in request.args['sort']:
            #   Ascending Date
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(asc(Event.date))  )
            
        elif 'date_desc' in request.args['sort']:
            #   Descending Date
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(desc(Event.date))  )
            
        else:
            #   Default (Ascending ID Sort)
            evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(asc(Event.id))  )
            
        
        newevents = list()
        for event in evsort:
            image = event.image
            encoded_image = base64.b64encode(image).decode("utf-8")
            image = f"data:image/png;base64,{encoded_image}"
            event.image = image
            newevents.append(event)

        return render_template('searchresults.html', events=newevents)
    
    else:
        return redirect(url_for('main.index'))



#--Type Filter Route
@mainbp.route('/typefilter')
def typefilter():
    if request.args['search'] and request.args['search'] != "":
        
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        events = db.session.scalars( db.select(Event).where( (Event.type.like(query)) ) )
        
        newevents = list()
        for event in events:
            image = event.image
            encoded_image = base64.b64encode(image).decode("utf-8")
            image = f"data:image/png;base64,{encoded_image}"
            event.image = image
            newevents.append(event)
            
        if (newevents.__len__() > 0):
            return render_template('searchresults.html', events=newevents)
        else:   
            return render_template('nosearchresults.html')
        
    else:
        return redirect(url_for('main.index'))