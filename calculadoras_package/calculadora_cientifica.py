from .calculadora import Calculadora


class calCientifica(Calculadora):
    PI = 3.1416

    def __init__(self, numero1=0, numero2=0):
        super().__init__()
    
    def circunferencia(self, radio):
        return round((2 * self.PI) * radio, 2)

    def areaCirculo(self, radio):
        return round(self.PI * (radio**2), 2)

    def areaCuadrado(self, lado):
        return round(lado * lado, 2)
