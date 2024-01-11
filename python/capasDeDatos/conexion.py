from logger_base import log
# import psycopg2 as bd
from psycopg2 import pool
import sys

class Conexion:
    #una base de postgress
    _DATABASE =''
    _USERNAME=''
    _PASSWORD=''
    _DB_PORT=''
    _HOST=''
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    # _conexion =None
    # _cursor=None

    # @classmethod
    # def obtenerConexion(cls):
    #     if cls._conexion is None:
    #         try:
    #             cls._conexion=bd.connect(host=cls._HOST,user=cls._USERNAME,passwd=cls._PASSWORD,port=cls._DB_PORT,datbase=cls._DATABASE)
    #             log.debug(f'Conexión exitosa {cls._conexion}')
    #             return cls._conexion
    #         except Exception as e:
    #             log.debug(f'Ocurrio una excepcion {e}')
    #             sys.exit()
    #     else:
    #         return cls._conexion
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio  un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool
    @classmethod
    def obtenerConexion(cls):
        conexion=cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del poll: {conexion}')
        return conexion 
        
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

    # @classmethod
    # def obtenerCursor(cls):
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             log.debug(f'Se abrio correctamente el cursor:{cls._cursor}')
    #             return cls._cursor
    #         except Exception as e:
    #             log.debug(f'Ocurrio una excepción: {e}')
    #             sys.exit()
    #     else:
    #         return cls._cursor
        
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion() # hasta aqui debería de funcionar por que el límite son 5
    conexion6 = Conexion.obtenerConexion()

# if __name__ == '__main__':
#     Conexion.obtenerConexion()

