import math
import random
# from decimal import Decimal
x = 2
y = 3
z = 4
print(x+y)
print(40+2.3)

print('chai' + 'code')
print(x,y,z)

print(repr('chai'))
print(str('chai'))
print(('chai'))

print(math.floor(3.5))
print(math.trunc(-2.8))

print(0o20) # octal
print(0xFF) # hex

print(oct(789))
a = int('64',8)
print(a)

print(random.random())
print(random.randint(1,10))

l1 = [67,89,45,32,90]
print(random.choice(l1))

l2 = random.shuffle(l1)
print(l1)

print(0.1 + 0.1 + 0.1 - 0.3)

# result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# print(result)

setone = {1,2,3,4}
print(setone & {1,3})
print(setone | {1,3})
print(setone - {1,2,3,4})
print(type({}))



