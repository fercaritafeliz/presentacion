try:
    archivo = open('./cosas de curso/manejoDeArchivos/prueba.txt', 'w',encoding='utf8')
    archivo.write('agregamos información al archivo \n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')