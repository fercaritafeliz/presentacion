#profundizando sistemas numeración

#decimal
a=10
print((f'a: {a}'))


#binario
a=0b1010
print((f'a: {a}'))


#octal
a=0o12
print((f'a: {a}'))

a = 0xA
print((f'a: {a}'))

#Convertir tipo entero incluyendo la base
a=int('23',10)#decimal# este esta por default
a=int('10111',2)#binario
a=int('27',8)#octal
a=int('17',16)#hexadecimal
a=int('34',5)#base 5
print((f'a: {a}'))