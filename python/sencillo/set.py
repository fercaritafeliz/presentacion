# un set no maniene un orden

planetas={'Marte','Jupiter','Venus'}
print(planetas)
print(len(planetas))

print( 'Marte' in planetas)
planetas.add('Tierra')
print(planetas)
planetas.add('Tierra')
print(planetas)

# no permite duplicados 

planetas.remove('Tierra')
print(planetas)
# dicard no saca errores
planetas.discard('Tierra')
print(planetas)

planetas.clear()
print(planetas)


del planetas 
#ya se borró por lo tanto saca error 
print(planetas)