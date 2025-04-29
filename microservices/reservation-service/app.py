from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    from app.routes import reservation_bp
    app.register_blueprint(reservation_bp, url_prefix='/reservations')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    print("✅ DEBUG: Reservation Service running on port 5003")
    app.run(host='0.0.0.0', port=5003)
