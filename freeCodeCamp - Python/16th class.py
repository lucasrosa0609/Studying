# programming
# algorithms
# a set of rules or steps used to solve a problem
# data  structures
# a particular way of organizing data in a computer

# what is no a "collection"

# most of our variables have one value in them - when we put a new value in the
# variable, the old value is overwritten

x = 2
x = 4
print(x)
print()

# a list is a kind of collection

# a collection allows us to put many values in a single variable
# a collection is nice because we can carry all many values around in
# one convenient package

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']

# list constants

# list constants are surrounded by square brackets and the elements in the
# list are separated by commas.
# A list element can be any python object - even another list.
# A list can be empty

print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print([1, [5,6], 7])
print([])
print()

# we already use lists

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')
print()

# friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy new year:', friend)
print('Done!')
print()

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy new year:', x)
print('Done!')
print()

# looking inside lists
# just like strings, we can get at any single element in a list using
# a index specified in square brackets

friends = ['Joseph', 'Glenn', 'Sally']
#             0         1        2
print(friends[1])
print()

# lists are mutable
# strings are "immutable" - we cannot change the contents of a string - we must
# make a new string to make any change. Lists are "mutable" - we can change
# an element of a list using the index operator

fruit = 'Banana'
# fruit[0] = 'n' -> traceback error
x = fruit.lower()  # this does not change the original one, creates a copy
print(x)
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
print()

# how long is a list?
# the len() function takes a list as a parameter and returns the number of
# elements in the list. Actually len() tells us the number of elements
# of any set or sequence (such as a string)


greet = 'Hello Bob'
print(len(greet))
x = [1, 2, 3, 'joe', 99]
print(len(x))

# using the range function
# the range function returns a list of numbers that range from zero to one less
# than the parameter. We can construct an index loop using for and an integer iterator

print(range(4))
print(list(range(4)))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))
print(list(range(len(friends))))

# examples:
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print()

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
print()

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))


