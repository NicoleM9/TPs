import argparse
import json
from pathlib import Path
import sys

ARCHIVO = Path.home() / ".tareas.json"


def cargar_tareas():
    if ARCHIVO.exists():
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4)


def add_tarea(args):
    tareas = cargar_tareas()

    nueva = {
        "id": len(tareas) + 1,
        "descripcion": args.descripcion,
        "done": False,
        "priority": args.priority
    }

    tareas.append(nueva)
    guardar_tareas(tareas)

    if args.priority:
        print(f'Tarea #{nueva["id"]} agregada (prioridad: {args.priority})')
    else:
        print(f'Tarea #{nueva["id"]} agregada')


def listar_tareas(args):
    tareas = cargar_tareas()

    for t in tareas:
        if args.pending and t["done"]:
            continue
        if args.done and not t["done"]:
            continue
        if args.priority and t["priority"] != args.priority:
            continue

        estado = "x" if t["done"] else " "
        prioridad = f" [{t['priority'].upper()}]" if t["priority"] else ""

        print(f'#{t["id"]} [{estado}] {t["descripcion"]}{prioridad}')


def completar_tarea(args):
    tareas = cargar_tareas()

    for t in tareas:
        if t["id"] == args.id:
            t["done"] = True
            guardar_tareas(tareas)
            print(f'Tarea #{args.id} completada')
            return

    print("Error: tarea no encontrada")
    sys.exit(1)


def eliminar_tarea(args):
    tareas = cargar_tareas()

    for t in tareas:
        if t["id"] == args.id:
            confirm = input(f'¿Eliminar "{t["descripcion"]}"? [s/N] ')
            if confirm.lower() == "s":
                tareas.remove(t)
                guardar_tareas(tareas)
                print(f'Tarea #{args.id} eliminada')
            else:
                print("Cancelado")
            return

    print("Error: tarea no encontrada")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Gestor de tareas")

    # CLAVE: required=True
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # ADD
    p_add = subparsers.add_parser("add", help="Agregar tarea")
    p_add.add_argument("descripcion")
    p_add.add_argument("--priority", choices=["baja", "media", "alta"])
    p_add.set_defaults(func=add_tarea)

    # LIST
    p_list = subparsers.add_parser("list", help="Listar tareas")
    p_list.add_argument("--pending", action="store_true")
    p_list.add_argument("--done", action="store_true")
    p_list.add_argument("--priority", choices=["baja", "media", "alta"])
    p_list.set_defaults(func=listar_tareas)

    # DONE
    p_done = subparsers.add_parser("done", help="Completar tarea")
    p_done.add_argument("id", type=int)
    p_done.set_defaults(func=completar_tarea)

    # REMOVE
    p_remove = subparsers.add_parser("remove", help="Eliminar tarea")
    p_remove.add_argument("id", type=int)
    p_remove.set_defaults(func=eliminar_tarea)

    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
