from app.controllers.datos_controller import crear_area, obtener_areas

data = {
    "nombre": "Parque Nacional Natural Sierra Nevada",
    "categoria": "Parque Nacional",
    "departamento": "Magdalena",
    "municipio": "Santa Marta",
    "area_km2": 3830.0,
    "fecha_declaratoria": "1964"
}

crear_area(data)

areas = obtener_areas()
for a in areas:
    print(a.nombre, a.departamento)
