from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AreaProtegida(db.Model):
    __tablename__ = 'areas_protegidas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    departamento = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    area = db.Column(db.Float)

    def __init__(self, nombre, departamento, categoria, area):
        self.nombre = nombre
        self.departamento = departamento
        self.categoria = categoria
        self.area = area
