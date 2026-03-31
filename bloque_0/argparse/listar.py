import argparse
import os

# Crear parser
parser = argparse.ArgumentParser(
    description="Lista archivos de un directorio"
)

# Argumento opcional (directorio)
parser.add_argument(
    "directorio",
    nargs="?",
    default=".",
    help="Directorio a listar (por defecto: actual)"
)

# Flag para archivos ocultos
parser.add_argument(
    "-a", "--all",
    action="store_true",
    help="Incluir archivos ocultos"
)

# Filtro por extensión
parser.add_argument(
    "--extension",
    help="Filtrar por extensión (ej: .py)"
)

args = parser.parse_args()

# Intentar listar
try:
    archivos = os.listdir(args.directorio)

    for archivo in archivos:

        # Ocultos
        if not args.all and archivo.startswith("."):
            continue

        # Extensión
        if args.extension and not archivo.endswith(args.extension):
            continue

        ruta = os.path.join(args.directorio, archivo)

        # Mostrar directorios con /
        if os.path.isdir(ruta):
            print(archivo + "/")
        else:
            print(archivo)

except FileNotFoundError:
    print("Error: directorio no encontrado")
