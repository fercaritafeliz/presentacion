# profundizando en el tipo str
import math
from miclase import Miclase

# concatenación automatica
variable = 'adios'
mensaje='hola'+'Mundo'+variable
mensaje+= 'universidad' 'Python'
# print(mensaje)

# help(str)
# help(str.capitalize)
# help(math)
# help(Miclase)
# print(Miclase.__doc__)
# print(Miclase.__init__.__doc__)
# print(Miclase.mi_metodo.__doc__)
# print(Miclase.mi_metodo)
# print(type(Miclase.mi_metodo))

# mensaje1='asdfasdf'
# mensaje2=mensaje1.capitalize()
# print(mensaje1)
# print(mensaje2)
# print(hex(id(mensaje1)))
# print(hex(id(mensaje2)))

# print('.'.join([mensaje1,mensaje2]))

# #diccionario
# diccionario= {'nombre':'juan','apellido':'Perez','edad':'18'}
# llaves='-'.join(diccionario.keys())
# valores='-'.join(diccionario.values())
# print(llaves,valores)
# # help(str.split)

# cursos = 'java python javascript Angulas Spring excel'
# lista_cursos=cursos.split( ' ' )
# print(lista_cursos)

# lista_cursos=cursos.split( ' ' ,2)
# print(lista_cursos)

#dar formato a un string
# nombre='Juan'
# edad=28

# mensaje_con_formato='Mi nombre es %s y tengo %d años'%(nombre,edad)
# print(mensaje_con_formato)

# persona=('Karla','Gomez',5000.00)
# mensaje_con_formato='Hola %s %s. Tu sueldo es %2.f'%persona
# print(mensaje_con_formato)

nombre='juan'
edad=28
sueldo=3000
mensaje_con_formato='Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)
mensaje_con_formato='Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)
mensaje_con_formato='Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje_con_formato)

diccionario ={'nombre':'Ivan','edad':35,'sueldo':8000.00}
mensaje = 'Nombre {persona[nombre]}, Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensaje)

print(nombre,edad,sueldo,sep=', ')