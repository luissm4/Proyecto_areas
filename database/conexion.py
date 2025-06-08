import mysql.connector
from config.settings import DB_CONFIG

def obtener_conexion():
    return mysql.connector.connect(**DB_CONFIG)
