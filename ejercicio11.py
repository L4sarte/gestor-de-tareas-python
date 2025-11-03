estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Programación Python",
    "activa": True
}

print("La edad del/la estudiante es: ",estudiante['edad'])
info = f"El nombre del/la estudiante es: {estudiante['nombre']} y cursa: {estudiante['curso']})"
print(info)

estudiante["ciudad"] = "Madrid"
print(estudiante)