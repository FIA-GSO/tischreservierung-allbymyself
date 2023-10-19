import flask
from flask import request, jsonify
import sqlite3

 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect():
    conn = sqlite3.connect('buchungssystem.sqlite')
    conn.row_factory = dict_factory
    return conn.cursor()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API, dont panic! The answer is 42</p>'''

#TODO payload checken, db aufrufen
@app.route('/tables/free', methods=['GET'])
def all_tables():
    return jsonify(connect().execute('SELECT * FROM tische;').fetchall())

@app.route('/tables/addFreeTable', methods=['POST'])
def post_table():
    cursor = connect()
    # Führen Sie die INSERT-Abfrage aus
    cursor.execute('INSERT INTO tische (anzahlPlaetze, tischnummer) VALUES (42, 42)')
    # Bestätigen Sie die Änderungen in der Datenbank
    cursor.connection.commit()
    # Schließen Sie den Cursor
    cursor.close()
    # Geben Sie eine Erfolgsnachricht zurück
    return jsonify({'message': 'Tisch erfolgreich hinzugefügt'})


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()

{
    "anzahlPlaetze": 4,
    "tischnummer": 1
  },