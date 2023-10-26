from flask import Flask
from models import db
from controller import app as controller_app

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buchungssystem.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.register_blueprint(controller_app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
