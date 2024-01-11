print('Proporcione los siguientes datos del libro')

nombre=input('Proporcione el nombre de libro: ')
id=int(input('Proporcione el ID de libro: '))
precio = float(input('Proporcione el valor del libro'))
envioGratuito = input('Indica si el envío es gratuito (True/False)')

if envioGratuito == 'True':
    envioGratuito=True
elif envioGratuito=='False':
    envioGratuito = False
else:
    envioGratuito='Valor incorrecto, debe escribir True o False'

print(f'''
    Nobre:{nombre}
    Id:{id}
    Precio:{precio}
    Envío gratuito{envioGratuito}
''')