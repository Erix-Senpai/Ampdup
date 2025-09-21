from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.datetime import TimeField, DateField
from wtforms import SelectField, ValidationError
from datetime import time
from datetime import date



# creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    # linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")

class EventForm(FlaskForm):
    def FutureDateOnly(form, fields):
        if (fields.data):
            CurrentDate = date.today()
            if (fields.data <= CurrentDate):
                raise ValidationError("Event date must be 1 day prior to the current date.")
    EventTitle = StringField("Event Title", validators=[InputRequired(message="Must have an event title.")])
    EventDescription = TextAreaField("Event Description", validators=[InputRequired(message="Must have a description of the event.")])
    EventImage = FileField("Event Image", validators= [FileRequired(message="Must upload an image."), FileAllowed(['jpg', 'jpeg', 'png'], message="File type must be .png, .jpeg or .jpg.")])
    EventDate = DateField("Event Date", format="%Y-%m-%d", validators=[InputRequired(message="Must have a starting date of event."), FutureDateOnly])
    EventStartTime = TimeField("Event Start Time", format="%H:%M", default=time(0,0), validators=[DataRequired(message="Must have a starting time.")])
    EventEndTime = TimeField("Event End Time", format="%H:%M", default=time(23,59), validators=[DataRequired(message="Must have an ending time.")])
    EventLocation = StringField("Event Location", validators=[InputRequired(message="Must have a location for the event.")])
    EventType = SelectField("Event Type", choices=[(1, "Concert"),(2, "DJ Event"),(3, "Club Night"),(4, "Disco"),(5, "Classical"),(6, "Music Festival"),(7, "Gig")])
    EventStatus = SelectField("Event Status", choices=[(1, "Open"), (2, "Cancelled"), (3, "Sold Out"), (4, "Inactive")])
    

# User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Post')