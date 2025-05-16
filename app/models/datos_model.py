from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AreaProtegida(db.Model):
    __tablename__ = 'areas_protegidas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100))
    departamento = db.Column(db.String(100))
    municipio = db.Column(db.String(100))
    area_km2 = db.Column(db.Float)
    fecha_declaratoria = db.Column(db.String(50))
