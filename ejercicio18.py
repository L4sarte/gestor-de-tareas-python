# --- Definición de Funciones ---

def anadir_tarea(lista_tareas):
    """Añade una nueva tarea a la lista."""
    nueva_tarea = input("Ingrese una nueva tarea: ")
    lista_tareas.append(nueva_tarea)
    print("¡Tarea añadida!")
    # NO necesitas 'return lista_tareas' porque la lista se modifica directamente.

def ver_tareas(lista_tareas):
    """Muestra todas las tareas en la lista."""
    print("---Tus Tareas---")
    if len(lista_tareas) == 0:
        print("¡No tienes tareas pendientes!")
    else:
        for tarea in lista_tareas:
            print(tarea)
    # NO necesitas 'return lista_tareas' porque solo estás mostrando datos.

def guardar_tareas(lista_tareas):
    """Guarda la lista actual de tareas en el archivo 'tareas.txt'."""
    with open("tareas.txt", "w") as f:
        for tarea in lista_tareas:
            f.write(tarea + "\n")
    # NO necesitas 'return' aquí. La función solo "guarda".

def cargar_tareas():
    """
    Carga las tareas desde 'tareas.txt' al iniciar el programa.
    No recibe argumentos, pero RETORNA una lista.
    """
    try:
        with open("tareas.txt", "r") as f:
            lineas = f.readlines()
            # Esta línea limpia el "\n" de cada línea leída
            tareas_cargadas = [linea.strip() for linea in lineas]
            return tareas_cargadas
    except FileNotFoundError:
        # Si el archivo no existe, simplemente empieza con una lista vacía
        return []

# --- Lógica Principal del Programa ---

# 1. Carga las tareas UNA SOLA VEZ al iniciar.
tareas = cargar_tareas()

while True:
    print("\n--- MENÚ ---")
    print("1. Añadir una tarea")
    print("2. Ver todas tus tareas")
    print("3. Salir")
    opcion = input("¿Que quieres hacer?: ")

    if opcion == "1":
        anadir_tarea(tareas)

    elif opcion == "2":
        # ¡Aquí solo llamas a 'ver_tareas'!
        ver_tareas(tareas)

    elif opcion == "3":
        # 2. Guarda las tareas UNA SOLA VEZ al salir.
        guardar_tareas(tareas)
        print ("¡Adiós! Tus tareas han sido guardadas.")
        break

    else:
        print("Opcion no valida")