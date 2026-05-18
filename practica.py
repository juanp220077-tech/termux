import sqlite3

class Persona:
	def __init__(self,nombre):
		self.nombre = nombre
		self.__id_interno = "ID-999"
	def saludar(self):
		print(f"hola soy {self.nombre}")
class Estudiante(Persona):
	def __init__(self,nombre, carrera):
		super().__init__(nombre)
		self.carrera = carrera
	def mostrar_detalle(self):
		print(f"{self.nombre} estudia {self.carrera}")
alumno = Estudiante("Martin Puente", "diswño grafico")
alumno.saludar()
alumno.mostrar_detalle()
