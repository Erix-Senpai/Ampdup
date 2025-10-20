from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired, Regexp
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.datetime import TimeField, DateField
from wtforms import SelectField, ValidationError, DecimalField
from datetime import time
from datetime import date
from .models import User

import re


# creates the login information
class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[InputRequired("Please enter a valid email")])
    password=PasswordField("Password", validators=[InputRequired('Please enter your password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    first_name=StringField("First Name", validators=[InputRequired("Please enter your first name")])
    surname=StringField("Surname", validators=[InputRequired("Please enter your surname")])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    phone_number = StringField("Phone Number", validators=[InputRequired("Please enter a phone number"), Regexp(r'^\+?\d{9,15}$', message="Please enter a valid phone number with 9-15 digits")])
    street_address = StringField("Street Address", validators=[InputRequired("Please enter a street address)")])
    # linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match"), Length(min=6, message="Password must be at least 6 characters long")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")

class EventForm(FlaskForm):
    def FutureDateOnly(form, fields):
        if (fields.data):
            CurrentDate = date.today()
            if (fields.data <= CurrentDate):
                raise ValidationError("Event date must be 1 day prior to the current date.")
    def AcceptedPriceField(form, fields):
        if (fields.data):
            try:
                value = fields.data
                print(value)
                if re.match(r"^\d+\.\d{2}$", str(value)):
                    if (value < 0):
                        raise ValidationError(message="Price must be a positive value.")
                    if (int(value) > 1000000):
                        raise ValidationError(message="Price is over the limit of AUD$1,000,000. Please contact support for ticket with sales over AUD$1,000,000.")
                else:
                    raise ValidationError(message="Price must be in the format: $1234.56")
            except Exception:
                raise ValidationError(message="Price must be in the format: $1234.56")
                
    title = StringField("Event Title", validators=[InputRequired(message="Must have an event title.")])
    description = TextAreaField("Event Description", validators=[InputRequired(message="Must have a description of the event.")])
    image = FileField("Event Image", validators= [FileRequired(message="Must upload an image."), FileAllowed(['jpg', 'jpeg', 'png'], message="File type must be .png, .jpeg or .jpg.")])
    price = DecimalField("Entrance Fee ($)", places=2, validators=[InputRequired(message="Price must be in the format: $1234.56"), AcceptedPriceField])
    date = DateField("Event Date", format="%Y-%m-%d", validators=[InputRequired(message="Must have a starting date of event."), FutureDateOnly])
    startTime = TimeField("Event Start Time", format="%H:%M", default=time(0,0), validators=[DataRequired(message="Must have a starting time.")])
    endTime = TimeField("Event End Time", format="%H:%M", default=time(23,59), validators=[DataRequired(message="Must have an ending time.")])
    location = StringField("Event Location", validators=[InputRequired(message="Must have a location for the event.")])
    type = SelectField("Event Type", choices=[(1, "Concert"),(2, "DJ Event"),(3, "Club Night"),(4, "Disco"),(5, "Classical"),(6, "Music Festival"),(7, "Gig")], coerce=int)
    status = SelectField("Event Status", choices=[(1, "Open"), (2, "Cancelled"), (3, "Sold Out"), (4, "Inactive")], coerce=int)
    

# User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])


<<<<<<< HEAD



=======
class EventForm(FlaskForm):
    def FutureDateOnly(form, fields):
        if (fields.data):
            CurrentDate = date.today()
            if (fields.data <= CurrentDate):
                raise ValidationError("Event date must be 1 day prior to the current date.")
    def AcceptedPriceField(form, fields):
        if (fields.data):
            try:
                value = fields.data
                print(value)
                if re.match(r"^\d+\.\d{2}$", str(value)):
                    if (value < 0):
                        raise ValidationError(message="Price must be a positive value.")
                    if (int(value) > 1000000):
                        raise ValidationError(message="Price is over the limit of AUD$1,000,000. Please contact support for ticket with sales over AUD$1,000,000.")
                else:
                    raise ValidationError(message="Price must be in the format: $1234.56")
            except Exception:
                raise ValidationError(message="Price must be in the format: $1234.56")
                
    title = StringField("Event Title", validators=[InputRequired(message="Must have an event title.")])
    description = TextAreaField("Event Description", validators=[InputRequired(message="Must have a description of the event.")])
    image = FileField("Event Image", validators= [FileRequired(message="Must upload an image."), FileAllowed(['jpg', 'jpeg', 'png'], message="File type must be .png, .jpeg or .jpg.")])
    price = DecimalField("Entrance Fee ($)", places=2, validators=[InputRequired(message="Price must be in the format: $1234.56"), AcceptedPriceField])
    date = DateField("Event Date", format="%Y-%m-%d", validators=[InputRequired(message="Must have a starting date of event."), FutureDateOnly])
    startTime = TimeField("Event Start Time", format="%H:%M", default=time(0,0), validators=[DataRequired(message="Must have a starting time.")])
    endTime = TimeField("Event End Time", format="%H:%M", default=time(23,59), validators=[DataRequired(message="Must have an ending time.")])
    location = StringField("Event Location", validators=[InputRequired(message="Must have a location for the event.")])
    type = SelectField("Event Type", choices=[(1, "Concert"),(2, "DJ Event"),(3, "Club Night"),(4, "Disco"),(5, "Classical"),(6, "Music Festival"),(7, "Gig")], coerce=int)
    status = SelectField("Event Status", choices=[(1, "Open"), (2, "Cancelled"), (3, "Sold Out"), (4, "Inactive")], coerce=int)
    

# User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Post')
>>>>>>> 28ac7639d13deaaecdc7cbec551d06786cb22f27
