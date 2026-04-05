#!/usr/bin/env python3

import os
import argparse


# -------------------------
# Buscar enlaces rotos
# -------------------------
def find_broken(path):
    broken = []

    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full = os.path.join(root, name)

            # Detectar symlink roto
            if os.path.islink(full) and not os.path.exists(full):
                broken.append(full)

    return broken


# -------------------------
# Función principal
# -------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Detecta enlaces simbólicos rotos"
    )

    parser.add_argument("path", help="Directorio a analizar")
    parser.add_argument("--delete", action="store_true", help="Eliminar enlaces rotos")
    parser.add_argument("--quiet", action="store_true", help="Solo mostrar cantidad")

    args = parser.parse_args()

    broken = find_broken(args.path)

    # Modo silencioso
    if args.quiet:
        print(len(broken))
        return

    print(f"Buscando enlaces simbólicos rotos en {args.path}...\n")

    if not broken:
        print("No se encontraron enlaces rotos.")
        return

    print("Enlaces rotos encontrados:")

    for b in broken:
        try:
            target = os.readlink(b)
        except OSError:
            target = "desconocido"

        print(f"  {b} -> {target} (no existe)")

        # Eliminación opcional
        if args.delete:
            resp = input("¿Eliminar? [s/N]: ").strip().lower()
            if resp == 's':
                try:
                    os.remove(b)
                    print("  Eliminado.")
                except Exception:
                    print("  Error al eliminar.")

    print(f"\nTotal: {len(broken)} enlaces rotos")


# -------------------------
if __name__ == "__main__":
    main()
