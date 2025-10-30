from .test import Index_Populate_Event_1
from . import db
from .models import Event
import base64
def Populate_Event():
    query = Event.query.all()
    event_list = []
    n = 0
    for events in query:
        image = events.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        event = {
            "id": events.id,
            "title": events.title,
            "description": events.description,
            "image": image,
            "price": events.price,
            "ticket": events.ticket,
            "ticket_remain": events.ticket_remain,
            "date": events.date,
            "startTime": events.startTime,
            "endTime": events.endTime,
            "location": events.location,
            "type": events.type,
            "status": events.status,
            "statusCode": events.statusCode
        }
        event_list.append(event)
    return event_list

