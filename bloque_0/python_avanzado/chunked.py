
from typing import Iterable, Iterator, List, TypeVar
from itertools import islice

T = TypeVar("T")


def chunked(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    """
    Divide un iterable en bloques (chunks) de tamaño fijo.

    Args:
        iterable: cualquier iterable (lista, string, generador, archivo, etc.)
        size: tamaño de cada chunk (debe ser > 0)

    Yields:
        List[T]: listas de hasta 'size' elementos
    """
    if size <= 0:
        raise ValueError("size debe ser mayor a 0")

    it = iter(iterable)

    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk

if __name__ == "__main__":
    # 🔹 Caso 1: lista
    print("Lista:")
    print(list(chunked(range(10), 3)))

    # 🔹 Caso 2: string
    print("\nString:")
    print(list(chunked("abcdefgh", 3)))

    # 🔹 Caso 3: iterable grande (simulación)
    print("\nPrimeros chunks de un generador:")
    gen = (x for x in range(100))
    for chunk in chunked(gen, 5):
        print(chunk)
        if chunk[0] >= 10:
            break

    # 🔹 Caso 4: archivo (simulado con lista de líneas)
    print("\nSimulación archivo:")
    lineas = ["linea1\n", "linea2\n", "linea3\n", "linea4\n"]
    for chunk in chunked(lineas, 2):
        print(chunk)