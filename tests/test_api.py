from app.services.api_service import APIClient

cliente = APIClient()
datos = cliente.obtener_datos()

print(f"Se obtuvieron {len(datos)} registros.")
print(datos[0])  # Muestra el primer registro para ver la estructura
