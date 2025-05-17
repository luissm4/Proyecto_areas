from app.database.conexion import create_app
from app.services.api_service import obtener_datos_api, procesar_datos_api

app = create_app()

with app.app_context():
    datos = obtener_datos_api()
    procesar_datos_api(datos)
