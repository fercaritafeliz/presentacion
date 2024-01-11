def miFuncionEnPython(nombre,apellido):
    print('Saludos')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

miFuncionEnPython('Juan','Perez')
miFuncionEnPython('Karla','Lara')

def sumar(a,b):
    return a+b

resultado=sumar(5,3)
print(f'Resultado de la suma: {resultado}')


def sumar2(a=0,b=0):
    return a+b

print(sumar2())
print(sumar2(3,5))


#funciones con cantidad de variables desconocida

def listaNombres(*nombres):#Python lo recorre como tupla
    for nombre in nombres:
        print(nombre)

listaNombres('Juan','Karla','María','Ernesto')
#diccionarios con cantidad variables 
def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}: {valor}')
listarTerminos()
listarTerminos(IDE='Integrated Development Environment',PK='Primary Key')

listarTerminos(DBMS='Data Managment System')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan','Karla','Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')#aqui funciona por que es un string pero cada letra del string es iterable
desplegarNombres((10,11))# aqui funciona por que es una tupla
desplegarNombres([10,11])# aqui funciona por que es una lista

#Funciones recursivas
def factorial(numero):
    if numero ==1:
        return 1
    else:
        return numero*factorial(numero-1)


resultado = factorial(5)
print(f'resultado: {resultado}')