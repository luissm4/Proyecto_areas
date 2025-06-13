# Importa el conector de MySQL para Python
import mysql.connector
from config.settings import DB_CONFIG

# Importa la configuración de conexión desde el archivo de settings centralizado
def obtener_conexion():
    return mysql.connector.connect(**DB_CONFIG)
