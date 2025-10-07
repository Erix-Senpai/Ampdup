from .test import Index_Populate_Event_1
from . import db
from .event_db import Event
import base64
def Populate_Event():
    events_ = Event.query.all()
    events = []
    n = 0
    for event in events_:
        image = event.eventImage
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        event_ = {
            "eventUid": event.eventUid,
            "title": event.eventTitle,
            "description": event.eventDescription,
            "image": image,
            "ticket": event.eventTicket,
            "date": event.eventDate,
            "startTime": event.eventStartTime,
            "endTime": event.eventEndTime,
            "location": event.eventLocation,
            "type": event.eventType,
            "status": event.eventStatus,
            "statusCode": event.statusCode
        }
        events.append(event_)
    return events

