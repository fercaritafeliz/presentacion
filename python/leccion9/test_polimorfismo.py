from Empleado import Empleado
from Gerente import Gerente
def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

empleado = Empleado('Juan',5000)
imprimir_detalles(empleado)

gerente=Gerente('Karla',6000,'Sistemas')
imprimir_detalles(gerente)