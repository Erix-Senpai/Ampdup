from Ampdup_Codebase import db, create_app
from Ampdup_Codebase.models import User, Event, Comment, Booking

app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()

u   = User( name            = 'Example_User', 
            emailid         = 'user@email.com.au', 
            password_hash   = 'Example1'
            )

e   = Event(title       = 'Example_Event',
            description = 'This is an example event',
            image       = bytes(b'abc'),
            price       = 10.00,
            date        = '17th December',
            startTime   = '10am',
            endTime     = '1pm',
            location    = 'West End',
            etype       = 'Rock',
            status      = 'Open',
            statusCode  = 'OpenCode (?)'      
            )
        
db.session.add(u)
db.session.add(e)
db.session.commit()
print('Successful User Registration')

quit()