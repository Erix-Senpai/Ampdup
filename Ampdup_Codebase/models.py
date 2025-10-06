from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, LargeBinary

class User(db.Model):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	# password should never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long, depending on your hashing algorithm
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
    
    # string print method
    def __repr__(self):
        return f"Name: {self.name}"
    

class Event(db.Model):
    __tablename__ = "Event"
    eventUid = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    eventTitle = Column(String, nullable=False)
    eventDescription = Column(Text, nullable=False)
    eventImage = Column(LargeBinary, nullable=False)
    eventTicket = Column(Float, nullable=False)
    eventDate = Column(String, nullable=False)
    eventStartTime = Column(String, nullable=False)
    eventEndTime = Column(String, nullable=False)
    eventLocation = Column(String, nullable=False)
    eventType = Column(String, nullable=False)
    eventStatus = Column(String, nullable=False)
    statusCode = Column(String, nullable=False)

    comments = db.relationship('Comment', backref='Event')
	
    
    # string print method

    def __init__(self, title, desc, image, ticket, date, start, end, location, etype, status, code):
        self.eventTitle = title
        self.eventDescription = desc
        self.eventImage = image
        self.eventTicket = ticket
        self.eventDate = date
        self.eventStartTime = start
        self.eventEndTime = end
        self.eventLocation = location
        self.eventType = etype
        self.eventStatus = status
        self.statusCode = code

def upload_event(event_form):
    EventTitle = event_form.EventTitle.data
    EventDescription = event_form.EventDescription.data
    EventImage = event_form.EventImage.data
    EventImage = EventImage.read()
    EventTicket = event_form.EventTicket.data
    EventDate = event_form.EventDate.data
    EventDate = str(EventDate)
    EventStartTime = event_form.EventStartTime.data
    EventStartTime = str(EventStartTime)
    EventEndTime = event_form.EventEndTime.data
    EventEndTime = str(EventEndTime)
    EventLocation = event_form.EventLocation.data
    EventType = event_form.EventType.data
    match EventType:
         case 1: EventType = "Concert"
         case 2: EventType = "DJ Event"
         case 3: EventType = "Club Night"
         case 4: EventType = "Disco"
         case 5: EventType = "Classical"
         case 6: EventType = "Music Festival"
         case 7: EventType = "Gig"
         case  _ : EventType = "Concert"
    EventStatus = event_form.EventStatus.data
    match EventStatus:
         case 1:
            EventStatus = "Open"
            StatusCode = "badge1"
         case 2:
            EventStatus = "Cancelled"
            StatusCode = "badge2"
         case 3:
            EventStatus = "Sold Out"
            StatusCode = "badge3"
         case 4:
            EventStatus = "Inactive"
            StatusCode = "badge4"
         case  _ :
            EventStatus = "Inactive"
            StatusCode = "badge4"

    event = Event( EventTitle, EventDescription, EventImage, EventTicket, EventDate, EventStartTime, EventEndTime, EventLocation, EventType, EventStatus, StatusCode)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # string print method
    def __repr__(self):
        return f"Comment: {self.text}"