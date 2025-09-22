from flask import Flask
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'somesecretkey'
    # set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
    # initialise db with flask app
    #db.init_app(app)

    Bootstrap5(app)
    



    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import create_event
    app.register_blueprint(create_event.create_event_bp)
    from . import destinations
    app.register_blueprint(destinations.destbp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app