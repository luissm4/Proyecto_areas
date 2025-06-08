def mostrar_menu():
    print("------------------------------------")
    print("Sistema de Áreas Protegidas")
    print("------------------------------------")
    print("1. Cargar datos desde la API")
    print("2. Listar datos")
    print("3. Crear nuevo dato")
    print("4. Actualizar dato")
    print("5. Eliminar dato")
    print("6. Salir")
    print("------------------------------------")
    return input("Seleccione una opción: ")

def mostrar_areas(lista):
    for area in lista:
        print(f"{area['no']} - {area['area_protegida']} - {area['tipo_area']} - {area['ubicacion_latitud_longitud']} - {area['invasiones_previas']} - {area['año_ultima_invasion']} - {area['proximidad_urbana']} - {area['nivel_alerta']}")

def solicitar_dato(campo):
    return input(f"Ingrese {campo}: ")

def solicitar_entero(campo):
    while True:
        try:
            return int(input(f"Ingrese {campo} (numero): "))
        except ValueError:
            print("Por favor digite números.")

def mostrar_mensaje(mensaje):
    print(f">>> {mensaje}")

def solicitar_opcion_actualizacion():
    print("Seleccione el campo a actualizar:")
    print("------------------------------------")
    print("1. area_protegida")
    print("2. tipo_area")
    print("3. ubicacion_latitud_longitud")
    print("4. invasiones_previas")
    print("5. año_ultima_invasion")
    print("6. proximidad_urbana")
    print("7. nivel_alerta")
    print("------------------------------------")
    opciones = {
        "1": "area_protegida",
        "2": "tipo_area",
        "3": "ubicacion_latitud_longitud",
        "4": "invasiones_previas",
        "5": "año_ultima_invasion",
        "6": "proximidad_urbana",
        "7": "nivel_alerta"
    }
    eleccion = input("Ingrese el numero de la opcion: ")
    return opciones.get(eleccion)