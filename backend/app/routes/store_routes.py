from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

store_blueprint = Blueprint('store', __name__)

@store_blueprint.route('/buy', methods=['POST'])
@jwt_required()
def buy_item():
    data = request.get_json()
    item_name = data.get('item')
    user_id = get_jwt_identity()

    # Logic to deduct points and grant item
    return jsonify({'message': f'Item {item_name} purchased successfully!'}), 200
