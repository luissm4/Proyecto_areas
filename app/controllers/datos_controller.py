from database.conexion import obtener_conexion

def guardar_datos(data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for item in data:
        cursor.execute("""
            INSERT INTO areas_protegidas (no, area_protegida, municipio, area_declarada_en_la_jurisdiccion,declaratoria, plan_de_manejo_ambiental)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            area_protegida=VALUES(area_protegida),
            municipio=VALUES(municipio),
            area_declarada_en_la_jurisdiccion=VALUES(area_declarada_en_la_jurisdiccion),
            declaratoria=VALUES(declaratoria),
            plan_de_manejo_ambiental=VALUES(plan_de_manejo_ambiental)
        """, (
            item.get("no"),
            item.get("area_protegida"),
            item.get("municipio"),
            item.get("area_declarada_en_la_jurisdiccion"),
            item.get("declaratoria"),
            item.get("plan_de_manejo_ambiental")
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
        INSERT INTO areas_protegidas (no, area_protegida, municipio, area_declarada_en_la_jurisdiccion, declaratoria, plan_de_manejo_ambiental)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        dato["no"],
        dato["area_protegida"],
        dato["municipio"],
        dato["area_declarada_en_la_jurisdiccion"],
        dato["declaratoria"],
        dato["plan_de_manejo_ambiental"]
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_dato(no, campo, valor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = f"UPDATE areas_protegidas SET {campo} = %s WHERE no = %s"
    cursor.execute(query, (valor, no))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_dato(no):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM areas_protegidas WHERE no = %s", (no,))
    conexion.commit()
    cursor.close()
    conexion.close()
