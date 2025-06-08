from app.controllers.datos_controller import (
    procesar_datos,
    listar_datos,
    crear_dato,
    actualizar_dato,
    eliminar_dato
)
from app.views import view

def main():
    while True:
        opcion = view.mostrar_menu()

        if opcion == "1":
            procesar_datos()
            view.mostrar_mensaje("Datos cargados")
        elif opcion == "2":
            datos = listar_datos()
            if datos:
                view.mostrar_areas(datos)
            else:
                view.mostrar_mensaje("No hay datos")
        elif opcion == "3":
            crear_dato()
        elif opcion == "4":
            actualizar_dato()
        elif opcion == "5":
            eliminar_dato()
        elif opcion == "6":
            view.mostrar_mensaje("Saliendo del sistema")
            break
        else:
            view.mostrar_mensaje("Opción invalida")

if __name__ == "__main__":
    main()
