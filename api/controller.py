# controller.py
from flask import Flask, jsonify
from service import TischService, ReservierungService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

tisch_service = TischService()
reservierung_service = ReservierungService()

@app.route('/tische', methods=['GET'])
def get_all_tables():
    tables = tisch_service.get_all_tables()
    return jsonify(tables)

# Weitere Endpunkte...
