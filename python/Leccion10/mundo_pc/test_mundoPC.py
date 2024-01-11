from teclado import Teclado
from raton import Raton
from computadora import Computadora
from monitor import Monitor
from orden import Orden
teclado1=Teclado('HP','USB')
raton1 = Raton('HP','USB')
monito1=Monitor('HP',15)
computadora1=Computadora('HP',monito1,teclado1,raton1)
# print(computadora1)
teclado2=Teclado('Acer','Bluetooth')
raton2 = Raton('Acer','Bluetooth')
monito2=Monitor('Acer',27)
computadora2=Computadora('Acer',monito2,teclado2,raton2)
# print(computadora2)
teclado3=Teclado('Gamer','Bluetooth')
raton3 = Raton('Gamer','Bluetooth')
monito3=Monitor('Gamer',34)
computadora3=Computadora('Gamer',monito2,teclado2,raton2)
# print(computadora2)

computadoras1=[computadora1,computadora2]
orden1=Orden(computadoras1)
print(orden1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadoras2 = [computadora2,computadora3]
orden2 =Orden(computadoras2)
print(orden2)