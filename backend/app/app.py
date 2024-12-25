from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os

app = Flask(__name__)

# Setup secret key for JWT and database URI from environment variables
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "your-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", "sqlite:///pets.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# API Endpoints

# Get pet info
@app.route('/api/pet', methods=['GET'])
def get_pet():
    pet = Pet.query.first()  # Just fetch the first pet, you can expand this
    if pet:
        return jsonify({"name": pet.name, "type": pet.type})
    else:
        return jsonify({"message": "No pet found"}), 404

# Add a new pet
@app.route('/api/pet', methods=['POST'])
@jwt_required()
def add_pet():
    data = request.get_json()
    name = data.get('name')
    pet_type = data.get('type')

    # Validate data
    if not name or not pet_type:
        return jsonify({"message": "Missing pet name or type"}), 400

    new_pet = Pet(name=name, type=pet_type)
    db.session.add(new_pet)
    db.session.commit()

    return jsonify({"message": "Pet added successfully!"}), 201

# Register and login (Optional for JWT)
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    # Add user to database (implement this as needed)
    return jsonify({"message": "User registered successfully!"})

@app.route('/api/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Authenticate user logic (implement as needed)
    # Generate JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

if __name__ == "__main__":
    app.run(debug=True)
