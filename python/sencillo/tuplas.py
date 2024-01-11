# una tupla no es modificable
frutas=('Naranja','Plátano','Guayaba')

print(len(frutas))
print(frutas[0])

print(frutas[0:2])


for fruta in frutas:
    print(fruta, end=' ')




# frutas[0] ='Péra'
frutasLista=list(frutas)
frutasLista[0]='péra'
frutas =tuple(frutasLista)
print('\n',frutas)

#mala practica mejor escoger bien una lista si se van a cambiar valores 

del frutas
print(frutas)
#se borra igual que las listas