
# 'def' is a key word to use a function
# Python naming convention is to use lowercase, snake-case for:
# 1) variables 2) methods 3) functions


def say_hi(name, age):
    # line 12 has 27 as a number; 'str' converts the number to a string so it can concatenate
    print('Hello ' + name + ', you are ' + str(age) + ' years old.')


say_hi('Isaac', 27)
say_hi('Morgan', 27)

# Return Statements


def cube(num):
    return num*num*num


result = cube(5)
print(result)



