#manejo de valores ininitos
import math
from decimal import Decimal
#usando constructor float
infinito_posotivo = float('inf')
print(infinito_posotivo)
print(f'Es infinito: {math.isinf(infinito_posotivo)}')

infinito_negativo = float('-inf')
print(f'Es infinito: {math.isinf(infinito_negativo)}')
#usando modulo math
infinito_posotivo=math.inf
print(infinito_posotivo)
print(f'Es infinito: {math.isinf(infinito_posotivo)}')

infinito_negativo=-math.inf
print(infinito_negativo)
print(f'Es infinito: {math.isinf(infinito_negativo)}')

#usando modulo decimal
infinito_posotivo= Decimal('infinity')
print(infinito_posotivo)
print(f'Es infinito: {math.isinf(infinito_posotivo)}')

infinito_negativo= Decimal('-infinity')
print(infinito_negativo)
print(f'Es infinito: {math.isinf(infinito_negativo)}')