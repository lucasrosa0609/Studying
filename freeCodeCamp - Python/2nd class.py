# variables, expressions and statements

# constants - fixed values such as numbers, letters and strings are called constants
# because their value does not change

# numeric constantes are as you expect
# string constants use single quotes or double quotes (' or ")

print(123)
print(98.6)
print('Hello World')
print()

# variables r named place in the memory where a programmer can store data and later
# retrieve the data using the variable "name"
# programmers get to choose the names of the variables
# you can change the contents of a variable in a later statement

x = 12.2
y = 14
x = 100  # x will get the latest assignment we put on it

# python variable name rules
# must start with a letter or underscore_
# must consist of letter, numbers and underscores
# Case Sensitive

# good = spam eggs spam23 _speed
# bad = 23spam #sign var 12
# different: spam Spam SPAM

spam = 'x'
Spam = 'y'
SPAM = 'z'

print(spam, Spam, SPAM)
print()

# mnemonic variable Names: since we programmers are given a choice in how we choose
# our variable names, there is a bit of "best practice"
# we name variable to help us remember what we intend to store in them ("mnemonic
# = memori aid)
# this can confuse beginning students because well-named variables often "sound"
# so good that they must be keywords

x1q3z9ocd = 35.0  # a = 35.0  or hours = 35.0
x1q3z9afd = 12.50  # b = 12.50  or rate = 12.50
x1q3p9afd = x1q3z9ocd * x1q3z9afd  # c = a * b  or pay = hours * rate
print(x1q3p9afd)  # print(c)  or  print(pay)
print()

# sentences or lines

x = 2  # assignment statement
x = x + 2  # assignment with expression
print(x)  # print statement

# assign statements: assign a value to a variable using the assignment statement (=)
# an assignment statement consists of an expression on the right-hand side
# and a variable to store the result

x = 3.9 * x * (1 - x)

# the calculations will happen first on the () then out of it
