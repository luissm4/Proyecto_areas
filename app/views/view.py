def mostrar_datos(data):
    for item in data:
        print(f"{item['no']} - {item['area_protegida']} - {item['tipo_area']} - {item['ubicacion_latitud_longitud']} - {item.get('invasiones_previas',)} - {item.get('año_ultima_invasion')} - {item['proximidad_urbana']} - {item['nivel_alerta']}")

def mostrar_mensaje(msg):
    print(msg)

def pedir_dato():
    return {
        "no": input("no: "),
        "area_protegida": input("area_protegida: "),
        "tipo_area": input("tipo_area: "),
        "ubicacion_latitud_longitud": input("ubicacion_latitud_longitud: "),
        "invasiones_previas": input("invasiones_previas: "),
        "año_ultima_invasion": input("año_ultima_invasion: "),
        "proximidad_urbana": input("proximidad_urbana: "),
        "nivel_alerta": input("nivel_alerta: ")
    }
