from app.controllers.datos_controller import listar_datos, procesar_datos, crear_dato, actualizar, eliminar

def menu():
    print("\n=== Sistema de Áreas Protegidas ===")
    print("1. Cargar datos desde la API")
    print("2. Listar datos")
    print("3. Crear nuevo dato")
    print("4. Actualizar dato")
    print("5. Eliminar dato")
    print("6. Salir")

def ejecutar():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            procesar_datos()
        elif opcion == "2":
            listar_datos()
        elif opcion == "3":
            crear_dato()
        elif opcion == "4":
            actualizar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()
