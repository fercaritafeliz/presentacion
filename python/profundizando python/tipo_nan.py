import math
from decimal import Decimal
#Not a number
a=float('NaN')
print(a)

print(f'Es NaN (not a number)?: {math.isnan(a)}')

a=Decimal('NaN')
print(a)

print(f'Es NaN (not a number)?: {math.isnan(a)}')
