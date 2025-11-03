tareas = []

def anadir_tarea(tareas):
    nueva_tarea = input("Ingrese una nueva tarea: ")
    tareas.append(nueva_tarea)
    print("¡Tarea añadida!")
    return tareas


def ver_tareas(tareas):
    print("---Tus Tareas---")
    for tarea in tareas:
        print(tarea)
    return tareas

def guardar_tareas(tareas):
    with open("tareas.txt", "w") as f:
        for tarea in tareas:
            f.write(tarea + "\n")
    return guardar_tareas

while True:
    print("1. Añadir una tarea")
    print("2. Ver todas tus tareas")
    print("3. Salir")
    opcion = input("¿Que quieres hacer?: ")
    if opcion == "1":
        anadir_tarea(tareas)
    elif opcion == "2":
        ver_tareas(tareas)
    elif opcion == "3":
        guardar_tareas(tareas)
        print ("¡Adios!")
        break
    else:
        print("Opcion no valida")