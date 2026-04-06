
class Transaction:
    """
    Context manager que permite realizar cambios sobre un objeto
    y revertirlos automáticamente si ocurre una excepción.
    """

    def __init__(self, obj):
        self.obj = obj
        self._estado_inicial = None

    def __enter__(self):
        # Guardar estado inicial del objeto
        self._estado_inicial = vars(self.obj).copy()
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        # Si hubo excepción → revertir cambios
        if exc_type is not None:
            vars(self.obj).clear()
            vars(self.obj).update(self._estado_inicial)

        return False  # no suprime excepciones
    
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
        self.nombre = "Sin nombre"

if __name__ == "__main__":
    cuenta = Cuenta(1000)

    print("Saldo inicial:", cuenta.saldo)

    # 🔹 Transacción exitosa
    with Transaction(cuenta):
        cuenta.saldo -= 100
        cuenta.saldo -= 200

    print("Saldo después de transacción exitosa:", cuenta.saldo)

    # 🔹 Transacción con error
    try:
        with Transaction(cuenta):
            cuenta.saldo -= 100
            cuenta.nombre = "Test"
            raise ValueError("Error simulado")
    except ValueError:
        print("Se produjo una excepción")

    print("Saldo después de error:", cuenta.saldo)
    print("Nombre después de error:", cuenta.nombre)