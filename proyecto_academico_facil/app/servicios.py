# servicios.py
# Aqui estan las funciones para guardar, mostrar, buscar,
# actualizar y eliminar estudiantes.

import json
import os

ARCHIVO = "data/estudiantes.json"


def leer_estudiantes():
    if not os.path.exists(ARCHIVO):
        return []

    archivo = open(ARCHIVO, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    return datos


def guardar_estudiantes(estudiantes):
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
    archivo.close()

def validar_gmail(correo):
    if correo.endswith("@gmail.com"):
        return True
    else:
        return False


def crear_estudiante():
    estudiantes = leer_estudiantes()

    nombre = input("Nombre: ")
    carrera = input("Carrera: ")
    carnet = input("Carnet: ")
    correo = input("Correo: ")

    if validar_gmail(correo) == False:
        print("El correo debe terminar en @gmail.com")
        return

    if len(estudiantes) == 0:
        nuevo_id = 1
    else:
        nuevo_id = estudiantes[-1]["id"] + 1

    estudiante = {
        "id": nuevo_id,
        "nombre": nombre,
        "carrera": carrera,
        "carnet": carnet,
        "correo": correo
    }

    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes)

    print("Estudiante guardado correctamente.")

def listar_estudiantes():
    estudiantes = leer_estudiantes()

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print(
                "ID:", estudiante["id"],
                "- Nombre:", estudiante["nombre"],
                "- Carrera:", estudiante["carrera"],
                "- Carnet:", estudiante["carnet"],
                "- Correo:", estudiante["correo"]
            )


def buscar_estudiante():
    estudiantes = leer_estudiantes()
    nombre = input("Nombre a buscar: ").lower()
    encontrado = False

    for estudiante in estudiantes:
        if nombre in estudiante["nombre"].lower():
            print(estudiante)
            encontrado = True

    if encontrado == False:
        print("No se encontro el estudiante.")


def actualizar_estudiante():
    estudiantes = leer_estudiantes()

    carnet_buscar = input("Carnet del estudiante: ")

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["carnet"] == carnet_buscar:

            nombre = input("Nuevo nombre: ")
            carrera = input("Nueva carrera: ")
            correo = input("Nuevo correo: ")

            # Validar el nuevo correo
            if validar_gmail(correo) == False:
                print("El correo debe terminar en @gmail.com")
                return

            estudiante["nombre"] = nombre
            estudiante["carrera"] = carrera
            estudiante["correo"] = correo

            encontrado = True

    if encontrado:
        guardar_estudiantes(estudiantes)
        print("Estudiante actualizado.")
    else:
        print("No existe ese estudiante.")

def eliminar_estudiante():
    estudiantes = leer_estudiantes()

    try:
        id_buscar = int(input("ID del estudiante: "))
    except:
        print("El ID debe ser un numero.")
        return

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["id"] == id_buscar:
            estudiantes.remove(estudiante)
            encontrado = True
            break

    if encontrado:
        guardar_estudiantes(estudiantes)
        print("Estudiante eliminado.")
    else:
        print("No existe ese estudiante.")
