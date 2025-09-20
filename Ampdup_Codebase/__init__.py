from flask import Flask
from flask_bootstrap import Bootstrap5



def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Secret'
    
    Bootstrap5(app)

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import create_event
    app.register_blueprint(create_event.create_event_bp)
    from . import events
    app.register_blueprint(events.eventsbp)

    return app

