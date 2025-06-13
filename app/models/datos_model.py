# Importa la librería requests, URL de la API y función para obtener una conexión a la base de datos MySQL
import requests
from config.settings import API_URL
from database.conexion import obtener_conexion

# Función que obtiene los datos desde la API y los guarda en la base de datos
def guardar_datos():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception("Error al obtener los datos desde la URL")
    datos = response.json()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for dato in datos:
        cursor.execute("""
            INSERT INTO areas_protegidas
            (no, area_protegida, tipo_area, ubicacion_latitud_longitud,
             invasiones_previas, año_ultima_invasion, proximidad_urbana, nivel_alerta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            dato["no"], dato["area_protegida"], dato["tipo_area"], dato["ubicacion_latitud_longitud"],
            dato["invasiones_previas"], dato["año_ultima_invasion"],
            dato["proximidad_urbana"], dato["nivel_alerta"]
        ))
    conexion.commit()
    cursor.close()
    conexion.close()

# Función que obtiene todos los datos almacenados en la tabla `areas_protegidas`
def obtener_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM areas_protegidas")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

# Función que inserta un nuevo registro manualmente en la base de datos
def insertar_dato(dato):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO areas_protegidas
        (no, area_protegida, tipo_area, ubicacion_latitud_longitud,
         invasiones_previas, año_ultima_invasion, proximidad_urbana, nivel_alerta)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        dato["no"], dato["area_protegida"], dato["tipo_area"], dato["ubicacion_latitud_longitud"],
        dato["invasiones_previas"], dato["año_ultima_invasion"],
        dato["proximidad_urbana"], dato["nivel_alerta"]
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

# Función que actualiza un campo específico de un registro identificado por 'no'
def modificar_dato(no, campo, valor):
    campos_validos = [
        "area_protegida", "tipo_area", "ubicacion_latitud_longitud",
        "invasiones_previas", "año_ultima_invasion",
        "proximidad_urbana", "nivel_alerta"
    ]
    if campo not in campos_validos:
        raise ValueError("Campo inválido")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = f"UPDATE areas_protegidas SET {campo} = %s WHERE no = %s"
    cursor.execute(query, (valor, no))
    conexion.commit()
    cursor.close()
    conexion.close()

# Función que elimina un registro por su número identificador 'no'
def eliminar_por_id(no):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM areas_protegidas WHERE no = %s", (no,))
    conexion.commit()
    cursor.close()
    conexion.close()
