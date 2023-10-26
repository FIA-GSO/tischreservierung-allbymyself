# service.py
from repository import TischRepository, ReservierungRepository

class TischService:
    def __init__(self):
        self.repository = TischRepository()

    def get_all_tables(self):
        return self.repository.get_all_tables()

    # Weitere Geschäftslogik für Tische...

class ReservierungService:
    def __init__(self):
        self.repository = ReservierungRepository()

    def get_reservations_by_table(self, tischnummer):
        return self.repository.get_reservations_by_table(tischnummer)

    # Weitere Geschäftslogik für Reservierungen...
