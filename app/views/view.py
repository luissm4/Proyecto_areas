def mostrar_datos(data):
    for item in data:
        print(f"{item['no']} - {item['area_protegida']} - {item['municipio']} - {item['area_declarada_en_la_jurisdiccion']} - {item.get('declaratoria',)} - {item.get('plan_de_manejo_ambiental')}")

def mostrar_mensaje(msg):
    print(msg)

def pedir_dato():
    return {
        "no": input("no: "),
        "area_protegida": input("Área protegida: "),
        "municipio": input("Municipio: "),
        "area_declarada_en_la_jurisdiccion": input("Área declarada: "),
        "declaratoria": input("Declaratoria: "),
        "plan_de_manejo_ambiental": input("Plan de manejo ambiental: ")
    }
