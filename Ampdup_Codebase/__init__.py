from flask import Flask
from flask_bootstrap import Bootstrap5



import secrets
def create_app():
    app = Flask(__name__)
    
    Bootstrap5(app)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    from . import create_events
    app.register_blueprint(create_events.create_event_bp)

    from . import events
    app.register_blueprint(events.eventsbp)

    return app

