from app.models.datos_model import AreaProtegida, db

def crear_area(data):
    nueva_area = AreaProtegida(**data)
    db.session.add(nueva_area)
    db.session.commit()
    return nueva_area

def obtener_areas():
    return AreaProtegida.query.all()

def actualizar_area(id, data):
    area = AreaProtegida.query.get(id)
    if area:
        for key, value in data.items():
            setattr(area, key, value)
        db.session.commit()
    return area

def eliminar_area(id):
    area = AreaProtegida.query.get(id)
    if area:
        db.session.delete(area)
        db.session.commit()
    return area
