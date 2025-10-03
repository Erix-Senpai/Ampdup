## This is an example test.
# This should later be injected into SQL, and inside index_database the link to Index_Populate_Event_1 should be switched to SQL db too.
def Index_Populate_Event_1():
    # Return list of events. This should later be implemented into SQLAlchemy.
    # Note: When retrieving, it should update the status based on the date.
    return[
        {
            "title": "The Weeknd: After Hours Til Dawn Tour",
            "description": "The Weeknd is bringing the After Hours Til Dawn Tour to Brisbane's Suncorp Stadium. Experience his electrifying setlist with special guest Playboi Carti & special guest Mike Dean",
            "image": "static/img folder/the weeknd.jpg",
            "date": 2026-8-1,
            "startTime": 12-15,
            "endTime": 22-45,
            "location": "Suncorp Stadium",
            "type": "Concert",
            "status": "Open"
        },
        {
            "title": "DISCO! at Prohibition",
            "description": "Get your 90s outfit ready and DISCO! the night away at the Prohibition Nighclub.",
            "image": "static/img folder/disco.jpg",
            "date": 2026-6-16,
            "startTime": 18-10,
            "endTime": 23-30,
            "location": "Prohibition Nightclub",
            "type": "Disco",
            "status": "Sold Out"
        },
        {
            "title": "DJ with Dave",
            "description": "BRISBANE GET READY! DJ with Dave is coming with some awesome beats. Let's get this party started!",
            "image": "static/img folder/dj event.jpg",
            "date": 2026-5-6,
            "startTime": 18-00,
            "endTime": 23-30,
            "location": "Eatons Hill Hotel Grand Ballroom",
            "type": "Music Festival",
            "status": "Cancelled"
        },
        {
            "title": "The Melody Maniacs",
            "description": "Catch the upcoming sensations 'The Melody Maniacs' performing near your city!",
            "image": "static/img folder/gig.jpg",
            "date": 2025-12-31,
            "startTime": 17-45,
            "endTime": 2-00,
            "location": "Black Bear Lodge",
            "type": "Club Night",
            "status": "Inactive"
        }
    ]
def Post_Event_db():
    return(
        "DJ with Dave",
        "BRISBANE GET READY! DJ with Dave is coming with some awesome beats. Let's get this party started!",
        "static/img folder/dj event.jpg",
        2026-5-6,
        18-00,
        23-30,
        "Eatons Hill Hotel Grand Ballroom",
        "Music Festival",
        "Cancelled"
        )
Post_Event_db()