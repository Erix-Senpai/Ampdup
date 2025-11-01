from flask import Blueprint, render_template, request, redirect, url_for

# Registration
from .models import User, Booking, Comment, Event
from .forms import RegisterForm, CommentForm
from Ampdup_Codebase import db
from .return_query import return_event_query

mainbp = Blueprint('main', __name__ , template_folder='../templates')



@mainbp.route('/')
def index():
    query = Event.query.all()
    events = return_event_query(query)
    return render_template('index.html', events = events, active_page='Home')

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


@mainbp.route('/trigger500') #Create a route to trigger a 500 error
def trigger500():
    # Force a runtime error
    1 / 0
    return "You’ll never see this"


#
# Searching, Sorting, and Filtering:
#
import base64
import sqlalchemy
from sqlalchemy import desc, asc

#--Search Route
@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        searchtext = str(request.args['search'])
        events = db.session.scalars( db.select(Event).where( (Event.title.like(query)) + (Event.description.like(query)) ) ) 
        newevents = return_event_query(events)
            
        if (newevents.__len__() > 0):
            return render_template('searchresults.html', events=newevents, searchtext=searchtext)
        else:   
            return render_template('nosearchresults.html', searchtext=searchtext)
        
    else:
        return redirect(url_for('main.index'))
    
  
  
#--Sort Route
@mainbp.route('/sort')
def sort():
    if request.args['sort'] and request.args['sort'] != "":
        sort_type = sort(request.args.get('sort'))
        evsort = db.session.scalars( db.select(Event).where(Event.status != 'Inactive').order_by(sort_type)) 
        newevents = return_event_query(evsort)
        if (newevents.__len__() > 0):
            return render_template('searchresults.html', events=newevents)
        else:   
            return render_template('nosearchresults.html')
    
    else:
        return redirect(url_for('main.index'))


#--Filter by Event Type (Type Filter) Route
@mainbp.route('/typefilter')
def typefilter():
    if request.args['search'] and request.args['search'] != "":
        
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        events = db.session.scalars( db.select(Event).where( (Event.type.like(query)) ) )
        
        newevents = return_event_query(events)
        if (newevents.__len__() > 0):
            return render_template('searchresults.html', events=newevents)
        else:   
            return render_template('nosearchresults.html')
    else:
        return redirect(url_for('main.index'))
    

#--Event Sorting Method
def sort(sort_key: str):
    sort_map = {
        "id_asc": asc(Event.id),
        "id_desc": desc(Event.id),
        "name_asc": asc(Event.title),
        "name_desc": desc(Event.title),
        "date_asc": asc(Event.date),
        "date_desc": desc(Event.date),
        "": asc(Event.id)
    }
    return sort_map.get(sort_key, asc(Event.id))