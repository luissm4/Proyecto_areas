import requests
from config.settings import API_URL

def obtener_datos_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return []
