import sys

suma = 0

for arg in sys.argv[1:]:
    try:
        numero = float(arg)
        suma += numero
    except ValueError:
        print(f"'{arg}' no es un número, se ignora")

print(f"Suma: {suma}")
