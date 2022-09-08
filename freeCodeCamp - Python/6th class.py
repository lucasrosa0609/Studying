# functions -> store and reuse

def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()
print()

# python functions
# there are two kinds of functions in python
# built-in functions that are provided as part of a Python - print(),
# input(), type(), float(), int()...
# functions that we define ourselves and then use
# we treat the built-in functions names as "new" reserved words (i.e.
# we avoid them as variable names)

# function definition
# in Python a function is some reusable code that takes arguments(s) as input, does
# some computation, and then return a result or results
# we define a function using the def reserved word
# we call/invoke the function by using the function name, parentheses and arguments
# in an expression

big = max('Hello word')
print(big)

tiny = min('Hello World')
print(tiny)

# max function

big = max('Hello world')
print(big)

# a function is some stored code that we use. A function takes some input and produces
# a output

# type conversion
# when you put a integer and floating point in a expression, the integer is
# implicitly converted to a float
# you can control this with the built-in functions int() and float()

print(float(99)/ 100)
i = 42
print(type(i))

f = float(i)
print(f)
print(type(f))
print(1 + 2 * float(3)/4-5)
print()

# string convertions
# you can also use int() and float() to convert between strings and integers
# you will get an error if the string does not contain numeric characters

sval = '123'
print(type(sval))
# print(sval+1)  # type error

ival = int(sval)
print(type(ival))
print(ival + 1)
nsv = 'Hello bob'
# niv = int(nsv) # Value error



