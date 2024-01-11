import psycopg2

conexion= psycopg2.connect(
    #conexión a base de datos postgres
    user='',
    password='',
    host='',
    port='',
    database=''
)

# print(conexion)
try:

    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada=input('Poporciona los id_persona a eliminar(separados por coma): ')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            # conexion.commit()# ya no se ocupa el commit por que usamos with
            resgistros_eliminados = cursor.rowcount
            print(f'Resgistros eliminados: {resgistros_eliminados}')
            # sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            # entrada=input('Poporciona el id_persona a eliminar: ')
            # valores=(entrada,)
            # cursor.execute(sentencia,valores)
            # # conexion.commit()# ya no se ocupa el commit por que usamos with
            # resgistros_eliminados = cursor.rowcount
            # print(f'Resgistros eliminados: {resgistros_eliminados}')
            # sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            # valores=(
            #     ('Juan ','Perez','jperez@gmail.com',1),
            #     ('Juan Carlos','Juarez','jcjuarez@gmail.com',2)
            # )
            # cursor.executemany(sentencia,valores)
            # # conexion.commit()# ya no se ocupa el commit por que usamos with
            # resgistros_insertados = cursor.rowcount
            # print(f'Resgistros insertados: {resgistros_insertados}')
            # sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            # valores=('Juan Carlos','Juarez','jcjuarez@gmail.com',1)            
            # cursor.execute(sentencia,valores)
            # # conexion.commit()# ya no se ocupa el commit por que usamos with
            # resgistros_Actualizados = cursor.rowcount
            # print(f'Resgistros insertados: {resgistros_insertados}')
            # sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            # valores=(
            #     ('Marcos','Cantu','mcantu@gmail.com'),
            #     ('Angel','Quintana','quintana@gmail.com'),
            #     ('Carlos','Lara','clara@gmail.com')
            #     )
            # cursor.executemany(sentencia,valores)
            # # conexion.commit()# ya no se ocupa el commit por que usamos with
            # resgistros_insertados = cursor.rowcount
            # print(f'Resgistros insertados: {resgistros_insertados}')
            # sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            # valores=('Carlos','Lara','clara@gmail.com')
            # cursor.execute(sentencia,valores)
            # # conexion.commit()# ya no se ocupa el commit por que usamos with
            # resgistros_insertados = cursor.rowcount
            # print(f'Resgistros insertados: {resgistros_insertados}')
            # sentencia='SELECT * FROM persona'
            # sentencia='SELECT id_persona,nombre FROM persona'
            # sentencia='SELECT * FROM persona WHERE id_persona=%s'
            # sentencia='SELECT * FROM persona WHERE id_persona IN %s'
            # entrada =input('Proporciona los Id\'s a buscar (separado por comas):')
            # llaves_primarias=(tuple(entrada.split(',')),) #se debe hacer una tupla de tuplas
            # # llaves_primarias =((1,2,3),)
            # cursor.execute(sentencia,llaves_primarias)
            # # id_persona =1
            # # cursor.execute(sentencia,(id_persona,))
            # # registros = cursor.fetchone()
            # registros = cursor.fetchall()
            # for registro in registros:
            #     print(registro)

            # print(registros)

    # cursor.close() # Este ya no por que se uso with en el cursor
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()