edad =int(input('Introduce tu edad:'))

veintes=edad >= 20 and edad <30
treintas=edad >= 30 and edad <40


if veintes or treintas:
    print('dentro de rango 20\'s o 30\'s')
    if veintes:
        print('Dentro de los 20\'s')
    elif treintas:
        print('Dentro de los 30\'s')
    else:
        print('Este caso no puede pasar')
else:
    print('fuera de rango 20\'s o 30\'s')