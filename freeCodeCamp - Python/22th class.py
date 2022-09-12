# sorting lists of tuples
# we  can take advantage of the ability to sort a list of tuples to get a sorted
# version of a dictionary.
# First we sdort the dictionary by the key using the items() method
# and sorted() function

d = {'a': 10, 'c': 1, 'b': 22}
print(d.items())
print(sorted((d.items())))
print()

# using sorted()
# we can do this even more directly usgin the built-in function sorted that
# takes a sequence as a parameter and returns a sorted sequence

t = sorted(d.items())

for k, v in sorted(d.items()):
    print(k, v)

print()


# sort by values instead of key
# if we could construct a list of tuples of the form (value, key) we could sort
# by value. We do this with a for loop that creates a list of tuples

c = {'a': 10, 'c': 1, 'b': 22}
tmp = list()
for k, v in c.items():  # for with k, v
    tmp.append((v, k))  # tuple with v, k (inverse)

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
print()

# top 10 most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():  # key, val
    newtup = (val, key)  # val, key (inverse)
    lst.append(newtup)

lst = sorted(lst, reverse=True)  # reverse!!!

for val, key in lst[:10]:  # for val, key
    print(key, val)  # print KEY, VAL (inverse again)
print()

# even shorter version
b = {'a': 10, 'c': 1, 'b': 22}
print(sorted([(v, k) for k, v in b.items()], reverse=True))
# list comprehension creates a dynamic list. In this case,
# we make a list of reversed tuples and then sort it.

