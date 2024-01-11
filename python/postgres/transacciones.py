import psycopg2 as bd

conexion= bd.connect(
    #base de datos postgres
    user='',
    password='',
    host='',
    port='',
    database=''
)

# print(conexion)
try:
    # conexion.autocommit=False# atuocommit en True es solo para pruebas
    
    with conexion:
        with conexion.cursor() as cursor:
            sentencia='INSERT INTO persona(nombr,apellido,email) VALUES(%s,%s,%s)'
            valores=('Maria','Ezparza','mesparza@gmail.com')
            cursor.execute(sentencia,valores)

            sentencia ='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valores('JUan Carlos','Juarez','jcjuarez',1)
            cursor.execute(sentencia,valores)

            # conexion.commit() #se debe usar si no esta el autocommit
            print('Termina la transacción') 
except Exception as e:
    # conexion.rollback()
    print(f'Ocurrio un error,se hizo rollback de la transacción: {e}')
finally:
    conexion.close()