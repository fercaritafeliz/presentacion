try:
    archivo = open('./cosas de curso/manejoDeArchivos/prueba.txt', 'r',encoding='utf8')
    #leer todo
    #print(archivo.read())
    #leer algunos caracteres
    # print(archivo.read(5))
    # print(archivo.read(3))
    #leer lineas completas
    # print(archivo.readline())
    # print(archivo.readline())
    #iterar el archivo
    # for linea in archivo:
    #     print(linea)
    #leer lineas #Este regresa una lista
    # print(archivo.readlines())
    #acceder a una linea de la lista
    # print(archivo.readlines()[0])
    archivo2=open('./manejoDeArchivos/copia.txt','a',encoding='utf8')
    archivo2.write(archivo.read())




except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
    print('se termina de leer y copiar archivos')