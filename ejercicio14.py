usuarios = [
    { "id": 1, "nombre": "Carlos", "email": "carlos@email.com" },
    { "id": 2, "nombre": "Maria", "email": "maria@email.com" },
    { "id": 3, "nombre": "Juan", "email": "juan@email.com" }
]

for usuario in usuarios:
    print(f"Usuario: {usuario["nombre"]}, Email: {usuario["email"]}")