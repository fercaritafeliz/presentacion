from NumerosIdenticosException import NumerosIdenticosException
resultado =None

try:
    a= int(input('Primer número: '))
    b=int(input('Segundo número:'))
    if(a==b):
        raise NumerosIdenticosException('Números identicos')
    
    resultado=a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}, {type(e)}') 
except TypeError as e:
    print(f'Ocurrio un error: {e}, {type(e)}') 
except Exception as e:
    print(f'Ocurrio un error: {e}, {type(e)}') 
else:
    print('No ocurrio ningun error')
finally:
    print('Ejecución del bloque finally')
print(f'Resultado: {resultado}')
print('Continuamos...')