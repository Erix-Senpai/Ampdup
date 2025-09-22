from flask import Flask
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)
    
    Bootstrap5(app)

    # A secret key for the session object
    app.secret_key = 'somerandomvalue'

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import create_event
    app.register_blueprint(create_event.create_event_bp)
    from . import destinations
    app.register_blueprint(destinations.destbp)
    from . import auth
    app.register_blueprint(auth.auth_bp)

    return app