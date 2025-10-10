from . import db
from datetime import datetime



class User(db.Model):
    __tablename__   = 'Users'
    id              = db.Column(db.Integer      ,  primary_key = True)
    user_name       = db.Column(db.String(20)   ,  unique=False, nullable=False)
    email           = db.Column(db.String(40)   ,  unique=False, nullable=False)
    password        = db.Column(db.String(20)   ,  unique=False, nullable=False)
    
    # Relationships
    comments        = db.relationship('Comment', backref='User')
    bookings        = db.relationship('Booking', backref='User')

    def __repr__(self):
        str = f"User {self.user_name}"
        return str




class Event(db.Model):    
    __tablename__   = 'Events'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(80))
    description     = db.Column(db.String(200))
    image           = db.Column(db.String(400))
    entryfee        = db.Column(db.Integer)
      
    # Relationships
    comments        = db.relationship('Comment', backref='Event')

    def __repr__(self):
        str = f"EventID: {self.id}, Event Name: {self.name}"
        return str
   
    
    
    
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
    __tablename__   = 'Comments'
    id              = db.Column(db.Integer, primary_key=True)
    text            = db.Column(db.String(400))
    created_at      = db.Column(db.DateTime, default=datetime.now())
    
    # Foreign Keys
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id        = db.Column(db.Integer, db.ForeignKey('Events.id'))
        
    def __repr__(self):
        str         = f"User {self.user}, \n Text {self.text}"
        return str
    
