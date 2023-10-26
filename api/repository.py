# repository.py
from models import Tisch, Reservierung

class TischRepository:
    def get_all_tables(self):
        return Tisch.query.all()

    # Weitere Methoden zum Zugriff auf Tische...

class ReservierungRepository:
    def get_reservations_by_table(self, tischnummer):
        return Reservierung.query.filter_by(tischnummer=tischnummer).all()

    # Weitere Methoden zum Zugriff auf Reservierungen...
