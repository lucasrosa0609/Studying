# functions of our own

# building our own functions we create a new function using the "def" keyword
# folowed by optional parameters in parentheses

# we indent the body of the function
# this defines the function but does not execute the body of the function

# storing a function

x = 5
print('Hello')


def print_lyrics():
    print("I am lumberjack, and I'm okay.")
    print('I sleep all night and i work all day.')


print('Yo')
x = x + 2
print(x)

print()
print()

# definitions and uses
# once we have defined a function, we can call (or invoke) it as many times as we like
# this is the store and reuse pattern


x1 = 5
print('Hello')
print('Yo')
print_lyrics()
x1 = x1 + 2
print(x1)
print()
# arguments
# an argument is a value  we pass into the function as its input when we call
# the function
# we use arguments so we can direct the function to do different kind of work when
# we call it at different times
# we put the arguments in parentheses after the name of the funtion

big = max('Hello World')  # 'Hello world is an argument

# parameter is a variable wich we use in the function definition. Its a "handle"
# that allows the code in the function to access the arguments for a particular
# function invocation

# def greet(lang):
#     if lang == 'es':
#         print('Hola')
#     elif lang == 'fr':
#         print('Bonjour')
#     else:
#         print('Hello')

# greet('en')
# greet('es')
# greet('fr')

# Return values
# Often a function will take its arguments, do some computation, and return a value to be used as the value of
# the function call in the calling expression. The return keyword is used for this

# def greet():
#     return "Hello"

# print(greet(), 'Glenn')
# print(greet(), 'Sally')

# a fruitful function is one that produces a result (or return value)
# the return statement end the function execution and "sends back" the result of the function


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')
print()

# arguments, parameters and results
# on big = max ('hello world') what happens is

# print(big)  # argument = 'Hello world'
# def max(inp):  # parameter
#    blah  # parameter
#    blah  # parameter
#    for x in y:  # parameter
#        blah  # parameter
#        blah  # parameter
#    return 'w'  # parameter
# 'w' = result

# multiple parameters / arguments
# we can define more tha none parameter in the function definition
# simply add more arguments when we call the function
# we match the number and order of arguments and parameters


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)
print()

# void (non-fruitful) Functions
# when a function does not return a value, we call it a void function
# functions that return values are fruitful functions
# void functions are not fruitful

# to function or not to function
# organize your code into "paragraphs" - capture a complete thought and "name it"
# dont repeat yourself - make it work once and then reuse it
# if something gets too long or complex, break it up into logical chunks and put
# those chunks in functions
# make a library of common stuff that you do over and over - perhaps share this with
# your friends
