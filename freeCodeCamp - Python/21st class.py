# tuples are like lists. Tuples are another kind of sequence that
# functions much like a list - they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
print()
y = (1, 9, 2)
print(max(y))
print()
for iter in y:
    print(iter)
    print()

# but tupler are "immutable". Unlike a list , once you create a tuple,
# you cannot alter its contents - similar to a string

# on a list:
x = [9, 8, 7]
x[2] = 6
print(x)
print()

# on a tuple it gives a traceback error
# z = (5,4,3)
# z[2] = 0

# tuples are more efficient. Since Python does not have to build tuple structures to
# be modifiable, they are simpler and more efficient in terms of memory use and
# performance than lists. So in our program when we are making "temporary variables"
# we prefer tuples over lists

# tuples and assignment: we can also put a tuple on the left-hand side of an
# assignment statement. We can even omit the parentheses

(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)
print()


# tuples and dictionaries

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k,v)

tups = d.items()
print(tups)
print()

# tuples are comparable
# the comparison operators work with tuples and other sequences.
# If the first item is equal, python goes on to the next element, and so on
# until it finds elements that differ

print((0, 1, 2) < (5, 1 ,2))
