import sqlite3

class Estudiante:
	def __init__(self, nombre, carrera):
		self.nombre = nombre
		self.carrera = carrera
	def guardar(self):
		conn = sqlite3.connect('ubolivar.db')
		cursor = conn.cursor()
		cursor.execute(" CREATE TABLE IF NOT EXISTS alumnos (nombre TEXT, carrera TEXT)")
		cursor.execute("INSERT INTO alumnos VALUES (?,?)",(self.nombre, self.carrera))
		print(f"Regisyro de: {self.nombre} guardado exitosamente.")
mi_alumno = Estudiante("Juan Puente","Informatica")
mi_alumno.guardar()
