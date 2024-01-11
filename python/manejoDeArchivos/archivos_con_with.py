# with open('./manejoDeArchivos/prueba.txt','r',encoding='utf8') as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('./cosas de curso/manejoDeArchivos/prueba.txt') as archivo:
    print(archivo.read())

