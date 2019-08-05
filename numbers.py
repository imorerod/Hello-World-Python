# pulls in many math functions
# 'math' is a 'module'
from math import *

print(2)
print(-2)
print(3 * 56)
# handles PEMDAS correctly
print(3 + 5 * 8)
# '%' is modulus operator; takes 10 / 3, then prints the remainder
print(10 % 3)

my_num = 5
print(my_num)
# makes my_num a string
# must use 'str' w/ numbers if concatenating with a string
print(str(my_num))

# absolute value
my_num = -5
print(abs(my_num))

# give this function a number and power
# 3 raised to the power of 2
print(pow(3, 2))

# tells which num is the largest
print(max(4,6))

# tells which num is the smallest
print(min(4,6))

# round the num
print(round(4.453))

# drops off the decimal place
print(floor(3.7))

# automatically rounds up to next whole number
print(ceil(4.358))

# finds square root
print(sqrt(56))
