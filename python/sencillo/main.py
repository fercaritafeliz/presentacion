

x=10
w=15.5
y='holi'
z=True
print(x)
print(id(x)) #Dirección de memoria 
#Tipos de datos---------------------------
print(type(x))  #int
print(type(y))  #str
print(type(z))  #bool
print(type(w))  #float

#cadena (String)

miGrupoFavorito = 'no se jajaja que imbécil'+' '+'A no cierto ... si cierto'
print(miGrupoFavorito + 'holi')
print('holi',miGrupoFavorito)

#tipos de boleanos-----------------------
miVariable=True
print(miVariable)

miVariable= 1>2

print(miVariable)

#etrada de usuario---------------------------
#resultado=input()#esto devuelve cadenas entonces debe convertirse a int() 
#print(resultado)

# operadores --------------------------------

opeA=3
opeB=2
suma = opeA+opeB
multi=opeA*opeB
divi=opeA/opeB
divi2=opeA//opeB
modulo=opeA%opeB
exponete=opeA**opeB
print(f'Resultado de la suma: {suma}')
print(f'Resultado de la multiplicación: {multi}')
print(f'Resultado de la división: {divi}')
print(f'Resultado de la división entera: {divi2}')
print(f'Resultado del residuo de la división: {modulo}')
print(f'Resultado de los exponentes: {exponete}')

#operadore de asignación----------------------------------
v =10
print(v)
v +=2
print(v)
v -=3
print(v)
v *=4
print(v)
v **=5
print(v)


#Operadores de comparación--------------------------------------

a=4
b=2

resultado= a == b
print(f'resultado de comparar {a} y {b} es : {resultado}')

resultado= a != b
print(f'resultado de comparar {a} y {b} es : {resultado}')

varA=int(input('Ingrese un número'))
if varA % 2 == 0:
    print('valor par')
else:
    print('valor impar')