# menu.py
# Este archivo muestra el menu del programa.

from app.servicios import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)


def main():
    opcion = ""

    while opcion != "0":
        print("\n===== SISTEMA ACADEMICO =====")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opcion incorrecta.")
