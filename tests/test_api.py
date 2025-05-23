from app.controllers.datos_controller import listar_datos, procesar_datos

def mostrar_menu():
    print("\n=== GESTIÓN DE ÁREAS PROTEGIDAS ===")
    print("1. Cargar datos desde API y guardarlos en MySQL")
    print("2. Listar datos desde MySQL")
    print("3. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            procesar_datos()
        elif opcion == "2":
            listar_datos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar()
