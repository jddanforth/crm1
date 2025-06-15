from flask import Flask
from .models import db
from .views import bp as main_bp


def create_app(config_object=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if config_object:
        app.config.from_object(config_object)
    db.init_app(app)
    app.register_blueprint(main_bp)
    with app.app_context():
        db.create_all()
    return app
