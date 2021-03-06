from .calculadora import Calculadora


class calEstandar(Calculadora):
    def __init__(self, numero1=0, numero2=0):
        super().__init__(numero1=numero1, numero2=numero2)

    def multiplicacion(self):
        return round(self.numero1 * self.numero2, 2)

    def exponente(self):
        return round(self.numero1 ** self.numero2, 2)

    def valorAbsoluto(self, numero):
        return abs(numero)
