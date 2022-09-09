# concatenating lists using +
# we can create a new list by adding two existing lists together

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print(c)
print()
# lists can be sliced using:

t = [9, 41, 12, 3, 74, 15]

print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print()

# remember: Just like in strings, the second number is "up to but no including"

# list methods
# x = list()
# type(x)
# dir(x)
# append, count, extend, index, insert, pop, remove, reverse, sort

# building a list from scratch
# we can create an empty list and then add elements using the append method
# the list stays in order and new elements are added at the end of the list

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
print()

# is something in a list?
# python provides two operators that let you check if an item is in a list
# these are logical operatores that return True or False
# they do not modify the list

some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)
print()

# lists are in order
# a list can hold many items and keep those items in the order until we do
# something to change the order. A list can be sorted (i.e., change its order).
# The sort method (unlike in strings) means "sorte yourself

friends = ['C', 'D', 'A', 'B']
friends.sort()
print(friends)
print(friends[0])
print()

# built-in functions and lists

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
print()

# different lists

# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'Done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total / count
# print('Average:', average)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)