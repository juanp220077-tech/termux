import sqlite3

class Estudiante:
	def __init__(self,nombre, carrera):
		self.nombre = nombre
		self.carrera = carrera
	def guardar(self):
		conn = sqlite3.connect('Unita.db')
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE estudiantes (nombre TEXT, carrera TEXT)")
		cursor.execute("INSERT INTO estudiantes VALUES (?,?)",(self.nombre, self.carrera))
		conn.commit()
		conn.close()
		print(f"Registro de: {self.nombre} guardado correctamente")
alumno_prueba = Estudiante("Martin Puente", "ingeniero de sistemas")
alumno_prueba.guardar()

