from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth_blueprint
    from app.routes.pet_routes import pet_blueprint
    from app.routes.store_routes import store_blueprint
    from app.routes.mini_games_routes import mini_games_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    app.register_blueprint(pet_blueprint, url_prefix='/api/pet')
    app.register_blueprint(store_blueprint, url_prefix='/api/store')
    app.register_blueprint(mini_games_blueprint, url_prefix='/api/mini-games')

    return app
