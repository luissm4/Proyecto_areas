from database.conexion import crear_conexion

class DatosModel:
    
    def guardar_dato(self, dato):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            sql = """
                INSERT INTO areas_protegidas (
                    area_protegida,
                    municipio,
                    area_declarada_en_la_jurisdiccion,
                    area_total_ha,
                    declaratoria,
                    plan_de_manejo_ambiental,
                    no_acuerdo_redelimitacion
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                dato.get("area_protegida", ""),
                dato.get("municipio", ""),
                dato.get("area_declarada_en_la_jurisdiccion", ""),
                dato.get("area_total_ha", ""),
                dato.get("declaratoria", ""),
                dato.get("plan_de_manejo_ambiental", ""),
                dato.get("no_acuerdo_redelimitacion", "")
            )
            cursor.execute(sql, valores)
            conn.commit()
        except Exception as e:
            print("Error al guardar:", e)
        finally:
            cursor.close()
            conn.close()
            
    def obtener_todos(self):
        try:
            conn = crear_conexion()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM areas_protegidas")
            return cursor.fetchall()
        except Exception as e:
            print("Error al obtener:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def actualizar_dato(self, id, nuevos_datos):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            sql = """
                UPDATE areas_protegidas SET
                    area_protegida = %s,
                    municipio = %s,
                    area_declarada_en_la_jurisdiccion = %s,
                    area_total_ha = %s,
                    declaratoria = %s,
                    plan_de_manejo_ambiental = %s,
                    no_acuerdo_redelimitacion = %s
                WHERE id = %s
            """
            valores = (
                nuevos_datos["area_protegida"],
                nuevos_datos["municipio"],
                nuevos_datos["area_declarada_en_la_jurisdiccion"],
                nuevos_datos["area_total_ha"],
                nuevos_datos["declaratoria"],
                nuevos_datos["plan_de_manejo_ambiental"],
                nuevos_datos["no_acuerdo_redelimitacion"],
                id
            )
            cursor.execute(sql, valores)
            conn.commit()
        except Exception as e:
            print("Error al actualizar:", e)
        finally:
            cursor.close()
            conn.close()

    def eliminar_dato(self, id):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM areas_protegidas WHERE id = %s", (id,))
            conn.commit()
        except Exception as e:
            print("Error al eliminar:", e)
        finally:
            cursor.close()
            conn.close()
