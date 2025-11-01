from sqlalchemy.orm import Query
import base64
# Used for obtaining query, and returning queried objects / tuples / etc. into a list of dicts for flexibility.

# Return Events Dict
def return_event_query(query: Query):
    event_list = []
    for events in query:
        image = events.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        e_list = {
            "event_id": events.id,
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
        event_list.append(e_list)
    return event_list

#Return Bookings, Events Dict
def return_booking_event_query(query: Query):
    event_list = []
    for bookings, events in query:
        image = events.image
        encoded_image = base64.b64encode(image).decode("utf-8")
        image = f"data:image/png;base64,{encoded_image}"
        e_list = {
            "booking_id": bookings.id,
            "event_id": events.id,
            "quantity": bookings.quantity,
            "order_date": bookings.order_date,
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
        event_list.append(e_list)

    return event_list

# Return Events Dict, Singular Query.
def return_single_event_query(events: Query):
    image = events.image
    encoded_image = base64.b64encode(image).decode("utf-8")
    image = f"data:image/png;base64,{encoded_image}"
    
    event_list = {
        "event_id": events.id,
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
    return event_list
