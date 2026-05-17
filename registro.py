import sqlite3

class Estudiante:
	def __init__(self,nombre, carrera):
		self.nombre = nombre
		self.carrera = carrera
	def guardar(self):
		conn = sqlite3.connect('Audla.db')
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (nombre TEXT, carrera TEXT)")
		cursor.execute("INSERT INTO alumnos VALUES (?,?)",(self.nombre, self.carrera))
		print(f"Registro de : {self.nombre} registrado com exito")
alumno_nuevo = Estudiante("Amir Puente","desarollo de software")
alumno_nuevo.guardar()
