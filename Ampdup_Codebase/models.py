from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, LargeBinary
from flask_login import UserMixin, current_user


class User(db.Model, UserMixin):
    __tablename__ = 'Users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, index=True, nullable=False)
    street_address = db.Column(db.String(200), nullable=False)
	# password should never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long, depending on your hashing algorithm
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
    
    # string print method
    def __repr__(self):
        return f"{self.first_name} {self.surname}"
    

class Event(db.Model):
    __tablename__ = "Events"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    image = Column(LargeBinary, nullable=False)
    price = Column(Float, nullable=False)
    ticket = Column(Integer, nullable=True)
    ticket_remain = Column(Integer, nullable=True)
    date = Column(String, nullable=False)
    startTime = Column(String, nullable=False)
    endTime = Column(String, nullable=False)
    location = Column(String, nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    statusCode = Column(String, nullable=False)

    comments = db.relationship('Comment', backref='event')
    owner_id = db.Column(db.Text, db.ForeignKey('Users.id'))
	
    
    # string print method

    def __init__(self, title, description, image, price, ticket, ticket_remain, date, startTime, endTime, location, etype, status, statusCode, owner_id):
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.ticket = ticket
        self.ticket_remain = ticket_remain
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.location = location
        self.type = etype
        self.status = status
        self.statusCode = statusCode
        self.owner_id = owner_id


def upload_event(event_form):
    title = event_form.title.data
    description = event_form.description.data
    image = event_form.image.data
    image = image.read()
    price = event_form.price.data
    ticket = event_form.ticket.data
    ticket_remain = ticket
    date = event_form.date.data
    date = str(date)
    startTime = event_form.startTime.data
    startTime = str(startTime)
    endTime = event_form.endTime.data
    endTime = str(endTime)
    location = event_form.location.data
    type = event_form.type.data
    match type:
         case 1: type = "Concert"
         case 2: type = "DJ "
         case 3: type = "Club Night"
         case 4: type = "Disco"
         case 5: type = "Classical"
         case 6: type = "Music Festival"
         case 7: type = "Gig"
         case _: type = "Concert"
    status = event_form.status.data
    match status:
         case 1:
            status = "Open"
            statusCode = "badge1"
         case 2:
            status = "Cancelled"
            statusCode = "badge2"
         case 3:
            status = "Sold Out"
            statusCode = "badge3"
         case 4:
            status = "Inactive"
            statusCode = "badge4"
         case  _ :
            status = "Inactive"
            statusCode = "badge4"
    owner_id = current_user.id
    event = Event(title, description, image, price, ticket, ticket_remain, date, startTime, endTime, location, type, status, statusCode, owner_id)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()



class Booking(db.Model):
    __tablename__   = 'Bookings'
    id              = db.Column(db.Integer, primary_key=True)       
    
    # Foreign Keys
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id        = db.Column(db.Integer, db.ForeignKey('Events.id'))

    def __repr__(self):
        str = f"EventID: {self.id}, Event Name: {self.name}"
        return str



class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))

    # string print method
    def __repr__(self):
        return f"Comment: {self.text}"
    


class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.now())

    event = db.relationship('Event', backref='orders')
    user = db.relationship('User', backref='orders')