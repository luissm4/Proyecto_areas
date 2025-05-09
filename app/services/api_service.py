import requests

class APIClient:
    API_URL = "https://www.datos.gov.co/resource/xpgq-dbtk.json"

    def obtener_datos(self, limite=100):
        response = requests.get(f"{self.API_URL}?$limit={limite}")
        response.raise_for_status()
        return response.json()

        