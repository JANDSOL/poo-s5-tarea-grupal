class Calculadora:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        return round(self.numero1 + self.numero2, 2)

    def resta(self):
        return round(self.numero1 - self.numero2, 2)

    def multiplicacion(self):
        return self.numero1 * self.numero2  # Sin round(), round() aplicar en polimorfismo.
                                            # clase calEstandar, archivo calculadora_estandar.py
    def division(self):
        if self.numero2 == 0: return 0
        else: return round(self.numero1 / self.numero2, 2)
