import sqlite3
from config.settings import DB_PATH 

def obtener_conexion():
    return sqlite3.connect(DB_PATH)
