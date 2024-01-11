numero = int(input('Ingresa un numero entre 1 y 4'))

numeroTexto=''
if numero ==1:
    numeroTexto='Numero uno'
elif numero ==2:
    numeroTexto='Numero dos'
elif numero ==3:
    numeroTexto='Numero tres'
elif numero ==4:
    numeroTexto='Numero cuatro'
else :
    numeroTexto='Valor fuera de rango'

print(f'Número proporcionado:{numero}: {numeroTexto}')