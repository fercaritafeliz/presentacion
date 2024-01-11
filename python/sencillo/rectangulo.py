class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calcularArea(self):
        return self.base*self.altura


reactangulo1=rectangulo(int(input('Introduce la base: ')),int(input('Introduce la altura: ')))

print(f'El area del rectangulo es: {reactangulo1.calcularArea()}')