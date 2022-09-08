# more conditional structures
# multi-way

x = 8
if x < 2:  # if x minor than 2:
    print('Small')
elif x < 10:  # in other way, if x minor than 10, but not minor than 2:
    print('Medium')
else:  # everything else that is not on the past statements:
    print('LARGE')
print('All Done')
print()

# no else:
x1 = 5
if x1 < 2:
    print('Small')
elif x1 < 10:
    print('Medium')

print('All done')
print()

# you can have many elif's

x2 = 100
if x2 < 2:  # first statement
    print('Small')
elif x2 < 10:  # if between 2 and 9
    print('Medium')
elif x2 < 20:  # if between 10 and 19
    print('Big')
elif x2 < 40:  # if between 20 and 39
    print('Large')
elif x2 < 100:  # if between 40 and 99
    print('Huge')
else:  # will only reach else, if everything before returns False
    print('Ginormous')

# multi-way puzzles
# wich will never print regardless of the value for x?

# option 1:
# x = 2
# if x < 2:
#     print('Below 2')
# elif x >= 2:
#     print('Two or more')
# else:
#     print('Something else')

# option 2:
# if x < 2:
#     print('Below 2')
# elif x < 20:
#     print('Below 20')
# elif x < 10:  # even if this is true, python will only take the first True
#     print('Below 10')
# else:
#     print("Something else")

# the try / except Structure
# you surround a dangerous section of code with try and except
# if the code in the try works - the except is skipped
# if the code in the try fails - it jumps to the except section

# cat notry.py
# astr = 'Hello bob'
# istr = int(astr)  # will have an Value Error here. Try / Except correct it
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)
print()

# problematic usage of Try / Except:

astr1 = 'Bob'
try:
    print('Hello')
    istr1 = int(astr)  # this will not generate an error, this will make except
    print('There')
except:
    istr1 = -1

print('Done', istr1)
print()

# more common usage:
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
else:
    print('Not a number')

# summary
# comparison operators: ==, <=, >=, >, <, != ; indentation, one-way decisions
# two-way decisions if: and else: ; nested decisions, multi-way decisions using elif
# try / except to compensate for errors


