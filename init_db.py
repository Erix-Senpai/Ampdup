from Ampdup_Codebase import db, create_app
from Ampdup_Codebase.models import User, Event, Comment, Booking

app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()

u   = User( user_name    = 'Example_User', 
            email        = 'user@email.com.au', 
            password     = 'Example1'
            )

e   = Event(name         = 'Example_Event',
            description  = 'This is an example event',
            image        = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag',
            entryfee     = 'R$10'
            )
        
db.session.add(u)
db.session.add(e)
db.session.commit()
print('Successful User Registration')

quit()