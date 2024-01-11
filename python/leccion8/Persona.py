class Persona:
    def __init__(self,nombre,edad) :
        self.nombre=nombre
        self.edad=edad

    def __add__(self,other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self,other):
        return self.edad-other.edad

obj1=Persona('Juan',14)
obj2=Persona('Carlos',16)

print(obj1+obj2)
print(obj1-obj2)
#Esta si

# Esta sintaxis no se debe de usar :v
# obj1.__add_(obj2)