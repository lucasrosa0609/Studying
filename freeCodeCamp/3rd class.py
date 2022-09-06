# expressions
# numeric expressions

# because of the lack of mathematical symbols on computer keyboards - we use computer speak to express the classic math
# operators

# asterisk is multiplication

# exponential (raise to a power) looks different than in math

# + adition ; - subtraction ; * multiplication ; / division ; ** power ; % Remainder


xx = 2
xx = xx + 2
print(xx)

yy = 440 * 2
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

# order of evaluation
# when we string operators together - Python must know wich one to do first
# this is called operator precedence
# wich operator takes precedence over the others?

x = 1 + 2 * 3 - 4 / 5 ** 6
# same as:
x1 = 1 + (2*3) - (4/(5**6))
print(x)
print(x1)
print()
# operator precedence rules
# highest precedence rule to lowest precedence rule:
    # parentheses are always respected
    # exponentiation (raise to a power)
    # multiplication, division, and remainder
    # addition and subtraction
    # left to right

# example:
# x = 1 + 2 ** 3 / 4 * 5
# x = 1 = 8 / 4 * 5  if they're on the same level, they will  be done left to right
# x = 1 + 2 * 5
# x = 1 + 10
# x = 11

# operator precedence
# reemember the rules top to bottom
# when writing code - use parentheses
# when writing code - keep mathematical expressions simple enought that they
# are easy to understand
# break long series of mathematical operations up to make them more clear

# what does "Type" Mean?
# in python variables, literals and constants have a "type"
# python knows the difference between an integer numebr and a string
# for example "+" means "addition" if something is a number and "concatenate" if
# something is a string (concatenate = put together)

ddd = 1 + 4
print(ddd)
eee = "Hello" + " " + "There"
print(eee)
print()

# Type matters
# python knows what "type" everything is
# some operations are prohibited
# you cannot "add 1" to a string
# we can ask python what type something is by using the type() function


try:
    eee = "Hello" + "There"
    eee = eee + 1
except:
    print('Type Error')
print()
print(type(eee))
print(type("Hello"))
print(type(1))
print()

# several types of numbers
# numbers have two main types
# integers are whole numbers:
    # -14, -2, 0, 1, 100, 401233
# Floating point numbers have decimal parts:
    # -2.5, 0.0, 98.6, 14.0
# there are other numebr typs - they are variations on float and integer
xx = 1
print(type(xx))
temp = 98.6
print(type(temp))
print(type(1))
print(type(1.0))
print()

# type convertions
# when you put a integer and floating point in a expression, the integer is
# implicitly converted to a float
# you can control this with the built-in functions int() and float()

print(float(99) + 100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
print()

# integer division
# integer division produces a floating point result

print(10/2)
print(9/2)
print(99/100)
print(10/2)
print()

# string conversions
# you can also use int() and float() to convert between strings and integers
# you will get an error if the string does not contain numeric characters

sval = '123'
print(type(sval))
# print(sval+1) -> type error
ival = int(sval)
print(type(ival))
print(ival+1)
nsv = "hello bob"
# niv = int(nsv) -> ValueError: invalid literal for int() with base 10: 'x'

# user input
# we can instruct python to pause and read data from the user using the input()
# the input() function returns a string

# nam = input('Who are you? ')
# print('Welcome', nam)

# converting user input
# if we want to read a number from user, we must convert it from a string to a
# number using a type conversion function
# later we will deal with bad input data

# inp = input('Europe floor? ')
# usf = int(inp) + 1
# print('US floor', usf)

# coments in python
# anything after a # is ignored by python
# why comment?
#  descibre what is going to happen in a sequence of code
#  document who wrote the code or other ancillary information
#  turn off a line of code - perhaps temporarily

# get the name of the file and open it
name = input('Enter the file:')
handle = open('name', 'r')

# count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# all done
print(bigword, bigcount)

# summary
# type, reserved words, variables(mnemonic), operators, operator precedence,
# integer division, conversion between types, user input, comments(#)