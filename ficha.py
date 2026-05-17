import sqlit3

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público
        self.__id_interno = "ID-999" # ENCAPSULAMIENTO (privado)

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# HERENCIA: Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre) # Llama al constructor del padre
        self.carrera = carrera

    def mostrar_detalle(self):
        print(f"{self.nombre} estudia {self.carrera}")

# Instanciación
alumno = Estudiante("Juan Puente", "Software")
alumno.saludar() # Método heredado
alumno.mostrar_detalle() # Método propio

