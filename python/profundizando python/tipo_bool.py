#tipos númericos False para 0 y true para demás valores
valor=0
resultado =bool(valor)

print(valor,f'resultado: {resultado}')

valor=0.0
resultado =bool(valor)

print(valor,f'resultado: {resultado}')
#tipo str
#cadena vacía false y demnas valores true
valor=''
resultado =bool(valor)

print(valor,f'resultado: {resultado}')

#tipo colecciones, false para colecciones vacias, true para todos los demas colecciones
#lista

valor=[]
resultado =bool(valor)

print(valor,f'resultado: {resultado}')
#tupla
valor=()
resultado =bool(valor)

print(valor,f'resultado: {resultado}')

#diccionario
valor={}
resultado =bool(valor)

print(valor,f'resultado: {resultado}')

if '':
    print('Regreso verdadero')
else:
    print('Regreso falso')