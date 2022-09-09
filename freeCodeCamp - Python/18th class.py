# best friends: strings and lists

abc = "With three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
print()

print(stuff)
for w in stuff:
    print(w)
print()

# split breaks a string into parts and produces a list of strings.
# We think of these as words. We can access a particular word on loop through
# all the words

line = 'A lot'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))
print()

# when you do not specify a delimiter, multiple spaces are treated
# like one delimiter. you can specify what delimiter character to use
# in the splitting

# e-mail adressing from stephen.marquard@uct.ac.za...

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])
# print()

# the double split pattern
# sometimes we split a line one way, and then grab one of the pieces of the line
# and split that piece again

str1 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = str1.split()
# print(words)
email = words[1]
# print(email)
pieces = email.split('@')
print(pieces)
print(pieces[1])


