# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tisch(db.Model):
    tischnummer = db.Column(db.Integer, primary_key=True, unique=True)
    anzahlPlaetze = db.Column(db.Integer)
    reservierungen = db.relationship('Reservierung', backref='tisch', lazy=True)

class Reservierung(db.Model):
    reservierungsnummer = db.Column(db.Integer, primary_key=True, unique=True)
    zeitpunkt = db.Column(db.String, nullable=False)
    tischnummer = db.Column(db.Integer, db.ForeignKey('tisch.tischnummer'), nullable=False)
    pin = db.Column(db.Integer, nullable=False)
    storniert = db.Column(db.Boolean, nullable=False, default=False)
