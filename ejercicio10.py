tareas = []

while True:
    tarea = input("Escriba una tarea (o 'fin' para terminar): ")
    if tarea == "fin":
        break
    else:
        tareas.append(tarea)

print("Tu lista de tareas es: ")
for tarea in tareas:
    print(tarea)
    