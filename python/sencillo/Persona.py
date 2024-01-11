class Persona:
    #pass esto para cuando quieres dejar la clase vacía
    def __init__(self,nombre,apellido,edad,*args,**kargs):
        self.__nombre=nombre #el doble guion bajo restringe los cambios a la variable
        #pero la notación que comunmente se encuentra es 1 solo guion bajo 
        # pero esto no omite la linea de codigo solo es cortesia profesional 
        self.__apellido=apellido
        self.__edad=edad
        self.args=args
        self.kargs=kargs
    
    def mostrarDetalle(self):
        print(f'{self.__nombre} {self.__apellido} {self.__edad} {self.args} {self.kargs}')
    
    @property # este decorador se usa para acceder indirectamente a la variable 
    def nombre(self):
        print('Lamando metodo get nombre')
        return self.__nombre
    
    #Si no se agrega el set entonces se dice que es variable de solo lectura 
    @nombre.setter
    def nombre(self,nombre):
        print('Lamando metodo set nombre')
        self.__nombre=nombre


    @property # este decorador se usa para acceder indirectamente a la variable 
    def apellido(self):
        print('Lamando metodo get apellido')
        return self.__apellido
    
    #Si no se agrega el set entonces se dice que es variable de solo lectura 
    @apellido.setter
    def apellido(self,apellido):
        print('Lamando metodo set apellido')
        self.__apellido=apellido


    @property # este decorador se usa para acceder indirectamente a la variable 
    def edad(self):
        print('Lamando metodo get edad')
        return self.__edad
    
    #Si no se agrega el set entonces se dice que es variable de solo lectura 
    @edad.setter
    def edad(self,edad):
        print('Lamando metodo set edad')
        self.__edad=edad

    def __del__(self):
        print(f'Persona: {self.__nombre}{self.__apellido}')



if __name__=='__main__':
    persona1= Persona('Juan','Perez',28,'2213295628',2,3,5, m='Manzana',p='pera')
    # print(persona1.nombre)
    # print(persona1.apellido)
    # print(persona1.edad)
    Persona.mostrarDetalle(persona1)
    persona1.__nombre='Juanin'# esto no se ejecuta por el encapsulamiento
    persona1.nombre='Juanin' # aquí se cambia por medio de un metodo y no directamente

    persona1.apellido='Sánchez'
    persona1.edad=2
    Persona.mostrarDetalle(persona1)
    persona1.mostrarDetalle()

    persona1.telefono='2213295628'
    print(persona1.telefono)
    # print(persona1.nombre)
    # print(persona1.apellido)
    # print(persona1.edad)

    persona2=Persona('Karla','Gomez',30)
    # print(persona2.nombre)
    # print(persona2.apellido)
    # print(persona2.edad)
    Persona.mostrarDetalle(persona2)
    # print(persona2.telefono)

    # print(f'{persona2.nombre},{persona2.apellido},{persona2.edad}')
    print(type(Persona))
    print(persona1.nombre)
    # no es correcto acceder de esta manera debido a que la variable esta encapsulada y podria aectar en otras cosas al programa

    print(__name__)