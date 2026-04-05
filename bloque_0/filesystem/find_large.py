#!/usr/bin/env python3

import os
import argparse

# -------------------------
# Parseo de tamaño (ej: 10K, 5M, 1G)
# -------------------------
def parse_size(size_str):
    units = {'K': 1024, 'M': 1024**2, 'G': 1024**3}

    size_str = size_str.strip().upper()

    if size_str[-1] in units:
        return int(size_str[:-1]) * units[size_str[-1]]
    
    return int(size_str)


# -------------------------
# Formato legible de tamaño
# -------------------------
def human(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


# -------------------------
# Función principal
# -------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Busca archivos/directorios grandes en un path"
    )

    parser.add_argument("path", help="Directorio a analizar")
    parser.add_argument("--min-size", default="0", help="Tamaño mínimo (ej: 10K, 5M, 1G)")
    parser.add_argument("--type", choices=['f', 'd'], help="f=archivos, d=directorios")
    parser.add_argument("--top", type=int, help="Mostrar solo los N más grandes")

    args = parser.parse_args()

    # Parsear tamaño mínimo
    try:
        min_size = parse_size(args.min_size)
    except ValueError:
        print("Error: tamaño inválido")
        return

    results = []

    # -------------------------
    # Recorrido recursivo
    # -------------------------
    for root, dirs, files in os.walk(args.path):

        if args.type == 'f':
            items = files
        elif args.type == 'd':
            items = dirs
        else:
            items = files + dirs

        for name in items:
            full = os.path.join(root, name)

            # Ignorar symlinks (opcional pero recomendable)
            if os.path.islink(full):
                continue

            try:
                size = os.path.getsize(full)

                if size >= min_size:
                    results.append((full, size))

            except (PermissionError, FileNotFoundError):
                continue

    # -------------------------
    # Ordenar por tamaño
    # -------------------------
    results.sort(key=lambda x: x[1], reverse=True)

    # Aplicar top N
    if args.top:
        results = results[:args.top]

    total = sum(size for _, size in results)

    # -------------------------
    # Mostrar resultados
    # -------------------------
    if not results:
        print("No se encontraron archivos que cumplan el criterio.")
    else:
        for path, size in results:
            print(f"{path} ({human(size)})")

    print(f"\nTotal: {len(results)} elementos, {human(total)}")


# -------------------------
if __name__ == "__main__":
    main()
