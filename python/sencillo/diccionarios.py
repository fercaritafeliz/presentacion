diccionario={
    'IDE':'Integrated Deveopment Environment',
    'OOP':'Oject oriented Programming',
    'DBMS':'Data Base Managment System'
}

print(diccionario)

print(len(diccionario))

print(diccionario['IDE'])
# esto es lo mismo pero mas largo
print(diccionario.get('OOP'))


diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# sin items no funiona este codigo para recrrer diccionarios
for termino, valor in diccionario.items():
    print(termino,valor)

for valor in diccionario.values():
    print(valor)

print('IDE' in diccionario)
# si hay e nuestro diccionao el termino

diccionario['PK']='Primary Key'
print(diccionario)

diccionario.pop('DBMS')
print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario
#muestra error por que ya se borró
print(diccionario)