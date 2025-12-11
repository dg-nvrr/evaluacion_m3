import json
import os

# nombre del archivo
ARCHIVO = "tareas.json"

def cargar_tareas():
    # carga tareas del json si existe
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def guardar_tareas(tareas):
    # guarda los cambio en el json
    try:
        with open(ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(tareas, f, indent=4)
    except:
        print("error al guardar")

def agregar_tarea(tareas):
    # pide descripcion y crea tarea
    desc = input("ingresa descripcion: ").strip()
    if desc:
        nueva = {"descripcion": desc, "completada": False}
        tareas.append(nueva)
        guardar_tareas(tareas)
        print("tarea agregada con exito")
    else:
        print("descripcion vacia no sirve")

def ver_tareas(tareas):
    # muestra lista de tareas
    print("\n--- lista de tareas ---")
    if not tareas:
        print("no hay tareas")
    else:
        for i, t in enumerate(tareas, start=1):
            estado = "[X]" if t["completada"] else "[ ]"
            print(f"{i}. {estado} {t['descripcion']}")
    print("-----------------------")

def marcar_completada(tareas):
    # cambia estado a completado
    ver_tareas(tareas)
    if not tareas: return

    try:
        idx = int(input("numero de tarea a completar: ")) - 1
        if 0 <= idx < len(tareas):
            tareas[idx]["completada"] = True
            guardar_tareas(tareas)
            print("listo, tarea completada")
        else:
            print("numero invalido")
    except ValueError:
        print("error: ingresa un numero")

def eliminar_tarea(tareas):
    # elimina tarea por indice
    ver_tareas(tareas)
    if not tareas: return

    try:
        idx = int(input("numero de tarea a eliminar: ")) - 1
        if 0 <= idx < len(tareas):
            borrada = tareas.pop(idx)
            guardar_tareas(tareas)
            print(f"tarea '{borrada['descripcion']}' eliminada")
        else:
            print("numero invalido")
    except ValueError:
        print("error: ingresa un numero")

def menu():
    # opciones del menu
    print("\n--- gestor de tareas ---")
    print("1. agregar tarea")
    print("2. ver tareas")
    print("3. marcar tarea como completada")
    print("4. eliminar tarea")
    print("5. salir")

def main():
    # flujo principal
    tareas = cargar_tareas()
    
    while True:
        menu()
        opc = input("elige opcion: ")

        if opc == '1': agregar_tarea(tareas)
        elif opc == '2': ver_tareas(tareas)
        elif opc == '3': marcar_completada(tareas)
        elif opc == '4': eliminar_tarea(tareas)
        elif opc == '5': break
        else: print("opcion no valida")

if __name__ == "__main__":
    main()