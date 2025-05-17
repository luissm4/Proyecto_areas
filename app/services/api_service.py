from app.controllers.area_dao import guardar_area

def procesar_datos_api(datos_api):
    for item in datos_api:
        guardar_area(item)
