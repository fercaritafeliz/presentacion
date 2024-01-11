from Persona import Persona

if __name__ == '__main__':
    print('Creacion objetos'.center(50,'-'))
    persona1=Persona('Karlangas','Mangas',20)
    persona1.mostrarDetalle()
    print('Eliminación objeto'.center(50,'-'))
    del persona1
    #esto destye el objeto para vaciar ese recurso pero es raro encontrarlo así
    





    print(__name__)