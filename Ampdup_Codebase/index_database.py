from .test import Index_Populate_Event_1
from . import db
from .models import Event
import base64
def Populate_Event():
    events_ = Event.query.all()
    events = []
    n = 0
    for event in events_:
        image = event.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        event_ = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "image": image,
            "price": event.price,
            "date": event.date,
            "startTime": event.startTime,
            "endTime": event.endTime,
            "location": event.location,
            "type": event.type,
            "status": event.status,
            "statusCode": event.statusCode
        }
        events.append(event_)
    return events

