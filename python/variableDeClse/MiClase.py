class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self,variable_insancia):
        self.variable_instancia=variable_insancia

    @staticmethod#un método estatico no puede acceder a self o sea a las variables de instancia
    def metodo_estatico():
        print(MiClase.variable_clase) #se pude acceder a las variables de clase


    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)



MiClase.metodo_clase()
miobjeto1 = MiClase('variable_instancia')
miobjeto1.metodo_clase()



MiClase.metodo_estatico()

miobjeto1.metodo_instancia()

print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

#esta variable se declara al vuelo
MiClase.variable_clase2 = 'Valor variable clase 2'

miClase2 = MiClase('Otro valor variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# no aparece como texto sugerido por que se crea al vuelo la variable
print(miClase.variable_clase2)# desde el objeto
print(MiClase.variable_clase2)#desde la clase

