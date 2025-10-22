from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import secrets

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    Bootstrap5(app)
    
    # A secret key for the session object
    app.secret_key = 'somerandomvalue'

    app.config['SECRET_KEY'] = secrets.token_hex(16)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ampdupdb.sqlite'
    db.init_app(app)


    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    from . import create_events
    app.register_blueprint(create_events.create_event_bp)

    from . import events
    app.register_blueprint(events.eventsbp)

    from . import auth
    app.register_blueprint(auth.auth_bp)

    from . import purchase_ticket
    app.register_blueprint(purchase_ticket.purchase_ticket_bp)

    from . import booking_history
    app.register_blueprint(booking_history.booking_history_bp)


    # initialise the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.scalar(db.select(User).where(User.id==user_id))

    return app

