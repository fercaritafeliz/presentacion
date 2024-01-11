from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool

class PersonaDAO:
    '''
    DAO DAA Access Object
    CRUD (create-read-update-delete)
    '''
    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR='DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        # with Conexion.obtenerConexion() as conexion:
            # with conexion.cursor() as cursor:
        with CursorDelPool as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas=[]
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)

    @classmethod
    def insertar(cls,persona):
        # with Conexion.obtenerConexion():
        #     with Conexion.obtenerCursor() as cursor:
        with CursorDelPool as cursor:
            log.debug(f'Persona a insertar: {persona}')
            valores=(persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
    @classmethod
    def actualizar (cls,persona):
        #  with Conexion.obtenerConexion():
        #     with Conexion.obtenerCursor() as cursor:
        with CursorDelPool as cursor:
            log.debug(f'Persona a actualizar: {persona}')
            valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        # with Conexion.obtenerConexion():
        #     with Conexion.obtenerCursor() as cursor:
        with CursorDelPool as cursor:
            valores=(persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'objeto eliminado: {persona}')
            return cursor.rowcount
if __name__ == '__main__':
    #Prueba de insertar 
    # persona1 = Persona (nombre='Pedro',apellido='Najera',email='pnajera@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # #prueba de actualizar 
    # persona1 = Persona(1,'juan Carlos', 'Juarez','cjjuarez@gmail.com')
    # personas_actualizados = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizados}')

    # #prueba eleiminar registro
    # persona1 = Persona(id_persona=20)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
     

    #Prueba de seleccionar 
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona) 