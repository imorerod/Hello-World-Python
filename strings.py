
# \n creates a line break
print('Uncle\nIsaac')

# \' creates a quotation in the middle of the string
print('Uncle\'Isaac')

phrase = 'Uncle Isaac'
print(phrase + ' is cool!')

# lower is a built-in function
print(phrase.lower())

# 'is' is an evaluator that produces boolean
print(phrase.islower())

# makes 'phrase' upper, then evaluates 'islower'
print(phrase.upper().islower())

# find 'length' of 'phrase'
print(len(phrase))

# reminder: index starts at 0
print(phrase[4])

# return index of 'U'
# if parameter not in 'phrase'; throws an err
print(phrase.index('U'))

print(phrase.replace('Isaac', 'I Mo'))




