import json
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False




# --- Definición de Funciones ---

def anadir_tarea(lista_tareas):
    # Añade una nueva tarea a la lista.
    descripcion_texto = input("Ingrese una nueva tarea: ")
    nueva_tarea_obj = Tarea(descripcion_texto)
    lista_tareas.append(nueva_tarea_obj)
    print("¡Tarea añadida!")
    # NO necesitas 'return lista_tareas' porque la lista se modifica directamente.

def ver_tareas(lista_tareas):
    # Muestra todas las tareas en la lista.
    print("---Tus Tareas---")
    if len(lista_tareas) == 0:
        print("¡No tienes tareas pendientes!")
    else:
        # enumerate(lista_tareas, start=1) hace que la cuenta empiece en 1
        for i, tarea_obj in enumerate(lista_tareas, start=1):
            estado = "[X]" if tarea_obj.completada else "[ ]"
            print(f"{i}. {estado} {tarea_obj.descripcion}")
            

def marcar_tarea(lista_tareas):
    # 1. Primero, mostramos las tareas para que el usuario vea los números
    ver_tareas(lista_tareas)
    
    # 2. Pedimos el número de la tarea que quiere marcar
    try:
        num_tarea = int(input("Ingresa el número de la tarea a marcar como completada: "))
        
        # 3. Validamos el número
        if 1 <= num_tarea <= len(lista_tareas):
            # Recordatorio: las listas empiezan en 0, por eso restamos 1
            tarea_a_marcar = lista_tareas[num_tarea - 1]
            
            # 4. ¡El poder de la POO! Modificamos el atributo del objeto
            tarea_a_marcar.completada = True
            print(f"¡Tarea '{tarea_a_marcar.descripcion}' marcada como completada!")
        else:
            print("Número de tarea fuera de rango.")
            
    except ValueError:
        print("Error: Debes ingresar un número.")


def guardar_tareas(lista_tareas):
    # Guarda la lista de OBJETOS Tarea en un archivo JSON.
    
    lista_para_json = []
    for tarea_obj in lista_tareas:
        # Convertimos cada Objeto Tarea en un diccionario
        diccionario_tarea = {
            "descripcion": tarea_obj.descripcion,
            "completada": tarea_obj.completada
        }
        lista_para_json.append(diccionario_tarea)
    
    # Abrimos el archivo .json en modo escritura ("w")
    with open("tareas.json", "w") as f:
        # Usamos json.dump() para "volcar" la lista de diccionarios en el archivo
        json.dump(lista_para_json, f, indent=4)

def cargar_tareas():
    # Carga la lista de tareas desde el archivo JSON y la convierte en Objetos Tarea.
    try:
        with open("tareas.json", "r") as f:
            # Usamos json.load() para leer el archivo JSON completo
            lista_de_diccionarios = json.load(f)
        
        lista_de_tareas = []
        # Recorremos la lista de diccionarios
        for diccionario in lista_de_diccionarios:
            # Creamos un Objeto Tarea usando los datos del diccionario
            tarea_obj = Tarea(diccionario["descripcion"])
            tarea_obj.completada = diccionario["completada"] # <-- ¡La clave!
            
            lista_de_tareas.append(tarea_obj)
            
        return lista_de_tareas
        
    except FileNotFoundError:
        # Si el archivo no existe, empezamos de cero
        return []
    except json.JSONDecodeError:
        # Si el archivo está vacío o corrupto, empezamos de cero
        return []

# --- Lógica Principal del Programa ---
tareas = cargar_tareas()

while True:
    print("\n--- MENÚ ---")
    print("1. Añadir una tarea")
    print("2. Ver todas tus tareas")
    print("3. Marcar tarea como completada") # <-- NUEVA
    print("4. Salir")                         # <-- NUEVA
    opcion = input("¿Que quieres hacer?: ")

    if opcion == "1":
        anadir_tarea(tareas)

    elif opcion == "2":
        ver_tareas(tareas)
    
    elif opcion == "3":                       # <-- NUEVA
        marcar_tarea(tareas)

    elif opcion == "4":                       # <-- NUEVA
        guardar_tareas(tareas)
        print ("¡Adiós! Tus tareas han sido guardadas.")
        break

    else:
        print("Opcion no valida")