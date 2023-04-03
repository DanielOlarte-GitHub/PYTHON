# Definir una lista vacía para las tareas
tareas = []

# Definir una función para agregar una tarea
def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

# Definir una función para eliminar una tarea
def eliminar_tarea():
    tarea = input("Ingrese la tarea que desea eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada.")
    else:
        print("La tarea ingresada no se encuentra en la lista.")

# Definir una función para mostrar la lista de tareas
def mostrar_tareas():
    print("\nLista de tareas:\n")
    for tarea in tareas:
        print("- " + tarea)

# Mostrar el menú y procesar la selección del usuario
while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    seleccion = int(input("Seleccione una opción: "))

    if seleccion == 1:
        agregar_tarea()
    elif seleccion == 2:
        eliminar_tarea()
    elif seleccion == 3:
        mostrar_tareas()
    elif seleccion == 4:
        break
    else:
        print("Seleccione una opción válida.")
