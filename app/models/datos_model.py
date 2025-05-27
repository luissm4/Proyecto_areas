from database.conexion import obtener_conexion

def guardar_datos(data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for item in data:
        cursor.execute("""
            INSERT INTO areas_protegidas (no, area_protegida, tipo_area, ubicacion_latitud_longitud,invasiones_previas, año_ultima_invasion, proximidad_urbana, nivel_alerta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            area_protegida=VALUES(area_protegida),
            tipo_area=VALUES(tipo_area),
            ubicacion_latitud_longitud=VALUES(ubicacion_latitud_longitud),
            invasiones_previas=VALUES(invasiones_previas),
            año_ultima_invasion=VALUES(año_ultima_invasion),
            proximidad_urbana=VALUES(proximidad_urbana),
            nivel_alerta=VALUES(nivel_alerta)       
        """, (
            item.get("no"),
            item.get("area_protegida"),
            item.get("tipo_area"),
            item.get("ubicacion_latitud_longitud"),
            item.get("invasiones_previas"),
            item.get("año_ultima_invasion"),
            item.get("proximidad_urbana"),
            item.get("nivel_alerta")
        )
        )
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM areas_protegidas")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def crear_dato_manual(dato):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO areas_protegidas (no, area_protegida, tipo_area, ubicacion_latitud_longitud, invasiones_previas, año_ultima_invasion, proximidad_urbana,nivel_alerta)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        dato["no"],
        dato["area_protegida"],
        dato["tipo_area"],
        dato["ubicacion_latitud_longitud"],
        dato["invasiones_previas"],
        dato["año_ultima_invasion"],
        dato["proximidad_urbana"],
        dato["nivel_alerta"]
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_dato(no, campo, valor):
    campos_validos = [
        'area_protegida',
        'tipo_area',
        'ubicacion_latitud_longitud',  
        'invasiones_previas',
        'año_ultima_invasion',
        'proximidad_urbana',
        'nivel_alerta'
    ]
    
    if campo not in campos_validos:
        raise ValueError(f"Campo inválido: {campo}")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = f"UPDATE areas_protegidas SET {campo} = %s WHERE no = %s"
    cursor.execute(query, (valor, no))
    conexion.commit()
    cursor.close()
    conexion.close()
