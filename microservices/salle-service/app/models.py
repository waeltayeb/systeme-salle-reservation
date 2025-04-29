from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Salle(db.Model):
    __tablename__ = 'salles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            "available": self.available
        }
