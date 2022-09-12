# matching and extracting data
# re.search() returns a True/False depending on whether the string matches the
# regular expression. If we actually want the matching string to be extracted,
# we use re.findall()

import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y)
# z = re.findall('[AIEUO]+', x)
#
# print(z)
# w = re.findall('[aeiou]+', x)
# print(w)

# warning: Greedy Matching
# the repear characters (*and+) push outward in bot directions (greedy) to match the
# largest possible string

x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)

# non-greedy matching
# not all regular expression repeat codes are greedy! If you add a ? character,
# the + and * chill out a bit

z = re.findall('^F.+?:', x)
print(y)
print()

# fine-tunning string extraction
# you can refine the match for re.findall() and separately determine
# which portion of the match is to be extracted by using parentheses

ex1 = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+', ex1)
print(y)
y1 = re.findall('^From (\S+@\S+)', ex1)
print(y1)
print()

