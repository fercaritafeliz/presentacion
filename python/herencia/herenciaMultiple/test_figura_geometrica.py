from cuadrad import Cuadrado
cuadrado1=Cuadrado(5,'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())
print(f'Cálculo área cuadrado: {cuadrado1.calcularArea()}')


#Metodo MRO - Method Reolution Order
print(Cuadrado.mro())
#Método para buscar en las clases hijas y padres
#y para difrenciar metodos de distintas clases