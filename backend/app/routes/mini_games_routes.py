from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

mini_games_blueprint = Blueprint('mini_games', __name__)

@mini_games_blueprint.route('/play', methods=['GET'])
@jwt_required()
def play_game():
    user_id = get_jwt_identity()

    # Logic for mini-game
    return jsonify({'message': 'Mini-game played! Rewards added.'}), 200
