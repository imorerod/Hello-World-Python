
for letter in 'Prime Digital Academy':
    print(letter)

friends = ['Jim', 'Pam', 'Kevin']
for friend in friends:
    print(friend)

# 0-9; 10 not included
for index in range(10):
    print(index)

# includes 3 but not 10
for index in range(3, 10):
    print(index)

# creates the range; which is whatever the length of the array is
# len(friends) = 3
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print('first iteration')
    else:
        print('not first iteration')



