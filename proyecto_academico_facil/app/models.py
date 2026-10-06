# models.py
# Aqui estan las clases del sistema.

class Estudiante:
    def __init__(self, id, nombre, carrera):
        self.id = id
        self.nombre = nombre
        self.carrera = carrera


class Docente:
    def __init__(self, id, nombre, materia):
        self.id = id
        self.nombre = nombre
        self.materia = materia


class Asignatura:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Curso:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
