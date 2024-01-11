class cubo:
    def __init__(self,lado):
        self.lado=lado

    def calcularVolumen(self):
        return self.lado**3


cubo1=cubo(int(input('Introduce el lado del cubo')))
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')
