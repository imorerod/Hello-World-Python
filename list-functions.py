
lucky_numbers = [24, 19, 11, 91, 27]
friends = ['Morgan', 'Miguel', 'Tyler', 'Ryan', 'Jacob']

# pushes 'lucky_numbers' to the end of 'friends' list
friends.extend(lucky_numbers)
print(friends)

# pushes Bob to end of 'friends' list
friends.append('Bob')

# insert Wesley at index 1
friends.insert(1, 'Wesley')

# remove value 'Bob'
friends.remove('Bob')

# gets rid of entire list
friends.clear()

# removes last value of list
friends.pop()

# give me (or not = error) the index of value 'Kevin'
print(friends.index('Kevin'))

# how many times value 'Tyler' occurs in list
print(friends.count('Tyler'))

# sort 'friends' list in ascending order
friends.sort()

# sort 'friends' list in descending order
friends.reverse()

# copies 'friends' list
friends2 = friends.copy()


