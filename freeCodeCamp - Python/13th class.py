# slicing strings
# we can also look at any continuous section of a string using a colon operator.
# The second number is nome beyond the end of the slice - 'op to but no including'.
# If the second number is beyoond the end of the string, it stops at the end

s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20])
print()

# if we leave off the first number or the last number of the slice,
# it is assumed to be the beginning or end of the string respectively

s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])
print()

# string concatenation
# when te + operator is applied to strings, it means concatenation

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)
print()

# using in as logical operator

# the in keyword can also be used to check to see if one string is "in" another string
# the in expression is a logical expression that returns
# True or False and can be used in an if statement

fruit = 'banana'
'n' in fruit
# true
'm' in fruit
# False
'nan' in fruit
# True
if 'a' in fruit:
    print('Found it!')
print()

# string comparison

# if word == 'banana':
#     print('All right, bananas')
#
# if word < 'banana':
#     print('Your word,' + word + ', comes before banana')
# elif word > 'banana':
#     print('Your word,' + word + ', comes after banana')
# else:
#     print('All right, bananas.')
print()

# string library
# python has a number of string functions which are in the string library.
# These functions are already built into every string - we invoke them by appending
# in the function to the string variable. These functions do not modify the original
# string, instead they return a new string that has been altered

greet = 'Hello bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())
print()

stuff = 'Hello world'
type(stuff)
dir(stuff)

# string library

# str.capitalize()
# str.center(width[, fillchar])
# str.endswith(suffix[, start[, end]])
# str.find(sub[, start[, end]])
# str.lstrip([chars])
# str.replace(old, new[, count])
# str.lower()
# str.rstrip([chars])
# str.strip([chars])
# str.upper()

# searching a string
# we use the find() function to search for a substring within another string.
# find() finds the first occurrence off the substring.
# If the substring is not found, find() returns -1.
# Remember that string position starts at zero

fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)
print()

# search and replace
# the replace() function is like a "search and replace" operation in a
# word processor. It replaces all occurrences of the search string with the
# replacement string

greet = 'Hello bob'
nstr = greet.replace('Bob','Jane')
print(greet)
print(nstr)
nstr1 = greet.replace('o', 'X')
print(nstr1)
print()

# stripping whitespace
# sometimes we want to take a string and remove whitespace at the beginning
# and/or end. lstrip() and rstrip() remove whitespace at the left or right.
# strip() removes both beginning and ending whitespace

greet = ' Hello Bob '
greet.lstrip()
# 'Hello Bob '
greet.rstrip()
# ' Hello Bob'
greet.strip()
# 'Hello Bob'

# only works with space

# prefixes

line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))
print()

# parsing and extracting
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)  # first space after atpos
print(sppos)
host = data[atpos+1: sppos]
print(host)

# two kinds of strings

# on python 3 all strings are unicode 

