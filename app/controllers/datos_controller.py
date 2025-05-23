from app.services.api_service import obtener_datos_api
from app.models.datos_model import DatosModel
from app.views.view import mostrar_datos

modelo = DatosModel()

def procesar_datos():
    datos_api = obtener_datos_api()
    for item in datos_api:
        modelo.guardar_dato(item)
    return modelo.obtener_todos()

def listar_datos():
    datos = modelo.obtener_todos()
    mostrar_datos(datos)

def actualizar_dato(id, nuevos_datos):
    modelo.actualizar_dato(id, nuevos_datos)

def eliminar_dato(id):
    modelo.eliminar_dato(id)
