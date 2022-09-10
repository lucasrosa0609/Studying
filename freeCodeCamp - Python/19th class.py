# python dictionaries

# a collection is nice because we can put more than one value in it and carry
# them all around in one convenient package.
# We have a bunch of values in a bunch of values in a single "variable".
# We do this by having more than one place "in" the variable.
# We have ways of finding the different places in the variable

# what is not a "collection"?

# most of our variables have one value in them - when we put a new value in the
# variable - the old value is ovewritten

x = 2
x = 4
print(x)
print()

# a story of two collections
# list - a linear collection of values that stay in order
# dictionary - a "bag" of values, each with its own label (things have keys)

# dictionaries are python's most powerful data collection.
# Dictionaries allow us to do fast database-like operations in Python.
# Dictionaries have different names in different languages
    # associative arrays - perl / PHP
    # properties or map or hashmap - java
    # property bag - c# / .net

# dictionaries
# lists index their entries based on the position in the list.
# Dictionaries are like bags - no order.
# So we index the things we put in the dictionary with a "looktup tag"

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
print()

# comparing lists and dictionaries
# dictionaries are like lists except that they use keys instead of numbers to
# look up values

first = list()
first.append(21)
first.append(183)
print(first)
first[0] = 23
print(first)
print()
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)
print()

# what changes is the indexing mechanism, lists have keys as positions and values,
# dict have keys as names and values

# dictionary literals (constants)
# dictionary literals use curly braces and have a list of key : value paris
# you can make an empty dictionary using empty curly bracers

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)
print()

# most common name?
# many counters with a dictionary
# one common use of dictionaries is counting how often we "see" something
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
print()

# dictionary tracebacks
# it is an error to reference a key which is not in the dictionary.
# We can use then in operator to see if a key is in the dictionary

# ccc = dict()
# print(ccc['csev'])

# when we see a new name, we need to add a new entry in the dictionary and
# if this the second or later time we have seen the name, we simply add one
# to the count in the dictionary under that name

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1

# print(counts)
print()

# get method for dictionaries
# the pattern of checking to see if a key is already in a dictionary
# and assuming a default value in the key is not there is so common that
# there is a method called get() that does this for us
# default value if key does not exist (and no traceback)

# if name in counts:
#     x = counts[name]
# else:
#     x = 0
#
# x = counts.get(name, 0)

# simplified counting with get()
# we can use get() and provide a default value of zero when the key is not yet in the
# dictionary - and then just add one

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)