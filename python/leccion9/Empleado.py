class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    
    def __str__(self) -> str:
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'