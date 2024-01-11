from Cuadrado import Cuadrado
#from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación Objeto Cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(5,'rojo')
print('Creación Objeto Rectangulo'.center(50,'-'))
rectangulo1=Rectangulo(5,4,'verde')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())
print(f'Cálculo área cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)
print('-'*50)
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(rectangulo1.color)
print(rectangulo1.calcularArea())
print(f'Cálculo área cuadrado: {rectangulo1.calcularArea()}')
print(rectangulo1)
cuadrado1.ancho=6
rectangulo1.ancho=8
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())
print(f'Cálculo área cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)
print('-'*50)
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(rectangulo1.color)
print(rectangulo1.calcularArea())
print(f'Cálculo área cuadrado: {rectangulo1.calcularArea()}')
print(rectangulo1)
#Metodo MRO - Method Reolution Order
print(Cuadrado.mro())# siendo abstracta cambia las gerarquias de clases :D
print(Rectangulo.mro())
#Método para buscar en las clases hijas y padres
#y para difrenciar metodos de distintas clases

# no se puede instanciar una clase abstracta
#figura = FiguraGeometrica()
