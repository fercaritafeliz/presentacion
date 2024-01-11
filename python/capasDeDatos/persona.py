from logger_base import log
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido =apellido
        self._email = email

    def __str__(self):
        return f'''
            Id: {self.id_persona}, Nombre: {self.nombre},
            apellido: {self.apellido}, email: {self.email}
         '''
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    #  Persona1=Persona(1,'juan','Perez','jperez@gmail.com')
    #  log.debug(Persona1)
    #  #simular un insert
    #  Persona1 = Persona(nombre='juan',apellido='Perez',email='jperez@gmail.com')
    #  log.debug(Persona1)
    #simular un delete
     Persona1=Persona(id_persona=1)     
     log.debug(Persona1)
