from flask import Flask
import secrets
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    from . import event
    app.register_blueprint(event.event_bp)

    from . import destinations
    app.register_blueprint(destinations.destbp)

    return app