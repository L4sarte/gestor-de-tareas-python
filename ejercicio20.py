class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.carrera = "Informática" # Podemos poner valores fijos también

e1 = Estudiante("Ana", 22)
e2 = Estudiante("Juan", 25)

print(f"{e1.nombre} tiene {e1.edad} años y estudia {e1.carrera}")
print(f"{e2.nombre} tiene {e2.edad} años y estudia {e2.carrera}")