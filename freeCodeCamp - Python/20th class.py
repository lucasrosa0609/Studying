# counting words in python

# counts = dict()
# print('Enter a line of text: ')
# line = input('')
#
# words = line.split()
# print('Words:', words)
#
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0)+ 1
#     print('Counts', counts)

# the general pattern to count the words in a line of text is
# to split the line into words, then loop through the words and
# use a dictionary to track the count of each word independently

# definite loops and dictionaries
# even though dictionaries are not stored in order, we can write a for
# loop that goes through all the entries in a dictionary - actually it goes
# through all the keys in the dictionary nad looks up the values

counts = {'Chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print()

# retrieving lists of keys and values
# you can get a list of keys, values or items(both) from a dictionary

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())  # gives a tuple
print()

# bonus: two iteration variables
# we loop through the key-value pairs in a dictionary using *two*
# iteration variables. Each iteration, the first variable is the key and
# the second variable is the corresponding value for the key

for v1, v2 in counts.items():
    print(v1, v2)

# the code on the first class

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

