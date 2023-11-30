from flask import Blueprint, jsonify, current_app
from service import TischService, ReservierungService

def create_controller_blueprint(database_uri):
    controller = Blueprint('controller', __name__)

    tisch_service = TischService()
    reservierung_service = ReservierungService()

    @controller.route('/', methods=['GET'])
    def reservierung():
        return "<h1>Hello, Kunde!</h1>"

    @controller.route('/tische', methods=['GET'])
    def get_all_tables():
        # Verwende current_app.config, um auf die Konfiguration der übergeordneten Anwendung zuzugreifen
        tables = tisch_service.get_all_tables()
        return jsonify(tables)

    @controller.route('/getjson', methods=['GET'])
    def get_all():
        # Verwende current_app.config, um auf die Konfiguration der übergeordneten Anwendung zuzugreifen
        payload = {
            "tisch": "2",
            "reserviert": "ja"
        }
        return jsonify(payload)

    return controller

