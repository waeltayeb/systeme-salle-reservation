from flask import Blueprint, jsonify
from app.models import Salle

salle_bp = Blueprint('salle', __name__)

@salle_bp.route('/', methods=['GET'])
def get_salles():
    salles = Salle.query.all()
    return jsonify([s.to_dict() for s in salles])
