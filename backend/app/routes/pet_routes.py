from flask import Blueprint, request, jsonify
from app.models.pet import Pet
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

pet_blueprint = Blueprint('pet', __name__)

@pet_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_pet():
    user_id = get_jwt_identity()
    pet = Pet.query.filter_by(owner_id=user_id).first()
    if pet:
        return jsonify({
            'name': pet.name,
            'health': pet.health,
            'happiness': pet.happiness,
            'energy': pet.energy
        })
    return jsonify({'message': 'No pet found'}), 404

@pet_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_pet():
    user_id = get_jwt_identity()
    data = request.get_json()
    name = data.get('name')

    new_pet = Pet(name=name, owner_id=user_id)
    db.session.add(new_pet)
    db.session.commit()

    return jsonify({'message': 'Pet created successfully'}), 201
