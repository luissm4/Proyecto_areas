from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.models.datos_model import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tu_contraseña@localhost/nombre_basedatos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
