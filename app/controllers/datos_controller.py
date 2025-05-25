from app.models.datos_model import guardar_datos, obtener_datos, crear_dato_manual, actualizar_dato, eliminar_dato
from app.services.api_service import obtener_datos_api
from app.views import view

def procesar_datos():
    datos = obtener_datos_api()
    guardar_datos(datos)
    view.mostrar_mensaje("Datos guardados.")

def listar_datos():
    datos = obtener_datos()
    view.mostrar_datos(datos)

def crear_dato():
    nuevo_dato = view.pedir_dato()
    crear_dato_manual(nuevo_dato)
    view.mostrar_mensaje("creado.")

def actualizar():
    no = input("Ingrese el número (no) del registro a actualizar: ")
    campo = input("Campo a actualizar (area_protegida, municipio, area_declarada_en_la_jurisdiccion, declaratoria, plan_de_manejo_ambiental ): ")
    valor = input("Nuevo valor: ")
    actualizar_dato(no, campo, valor)
    view.mostrar_mensaje("actualizado.")

def eliminar():
    no = input("Ingrese el número (no) del registro a eliminar: ")
    eliminar_dato(no)
    view.mostrar_mensaje("eliminado.")
def eliminar_dato(id):
    modelo.eliminar_dato(id)
