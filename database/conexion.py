import mysql.connector

def crear_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="areas_protegidas"
    )
