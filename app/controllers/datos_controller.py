from app.models.datos_model import guardar_datos, obtener_datos, insertar_dato, modificar_dato, eliminar_por_id
from app.views import view

def procesar_datos():
    guardar_datos()

def listar_datos():
    return obtener_datos()

def crear_dato():
    dato = {
        "no": view.solicitar_entero("número de ID"),
        "area_protegida": view.solicitar_dato("área protegida"),
        "tipo_area": view.solicitar_dato("tipo de área"),
        "ubicacion_latitud_longitud": view.solicitar_dato("latitud,longitud"),
        "invasiones_previas": view.solicitar_entero("número de invasiones previas"),
        "año_ultima_invasion": view.solicitar_entero("año de la última invasión"),
        "proximidad_urbana": view.solicitar_dato("proximidad urbana"),
        "nivel_alerta": view.solicitar_dato("nivel de alerta")
    }
    insertar_dato(dato)
    view.mostrar_mensaje("Creado exitosamente")

def actualizar_dato():
    no = view.solicitar_entero("número que va actualizar")
    campo = view.solicitar_opcion_actualizacion()
    if campo:
        valor = view.solicitar_dato(f"nuevo valor para {campo}")
        modificar_dato(no, campo, valor)
        view.mostrar_mensaje("actualizado.")
    else:
        view.mostrar_mensaje("Campo no válido.")

def eliminar_dato():
    no = view.solicitar_entero("número que va eliminar")
    eliminar_por_id(no)
    view.mostrar_mensaje("Dato eliminado.")