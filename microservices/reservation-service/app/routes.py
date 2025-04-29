from flask import Blueprint, jsonify
from app.models import Reservation

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([r.to_dict() for r in reservations])
