from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    salle_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time_deb = db.Column(db.String(20), nullable=False)
    time_fin = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "salle_id": self.salle_id,
            "date": self.date,
            "time_deb": self.time_deb,
            "time_fin": self.time_fin
        }
