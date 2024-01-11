from usuarioDAO import UsuarioDAO
from logger_base import log
from usuario import Usuario
opcion=None
while opcion!=5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')

    opcion=int(input('Escribe tu opción (1-5): '))
    if opcion==1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuarios)
    elif opcion==2:
        username_var=input('EScribe el username: ')
        password_var=input('EScribe el password: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuarios_insertados=UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion==3:
        id_usuario = int(input('Escribe el id_usuario a modificas:'))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Ecribe el nuevo password: ')  
        usuarios_actualizados = UsuarioDAO.actualizar(id_usuario)
        log.info(f'usuarios actualizados: {usuarios_actualizados}')
    elif opcion==4:
        id_usuario_var=int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario)
        usuarios_eliminados=UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicación')