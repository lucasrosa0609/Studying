# Conditional Execution
# if statement -> one way or another way

# conditional steps

x = 5
if x < 10:  # if the condition is True, the interpretation stops here, if not, continue
    print('Smaller')
if x > 20:  # in this case this line will not be executed
    print('Bigger')

print('Finis')
print()

# comparison operators
# boolean expressions ask a question and produce a yes or no result which we use to
# control program flow
# boolean expressions using comparison operators evaluate to True / False or
# Yes / No
# comparison operators look at variables but do not change the variables

# < Less than; <= Less than or equal to; == equal to; >= Greater than or Equal to
# > Greater than; != Not equal

x = 5
if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')
    print()

# one way decisions

x = 5
print('Before 5')
if x == 5:  # as long as you indent, it will keep executing everything indented
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Aftwerwards 5')
print('Before 6')
if x == 6:  # if it returns False, no running to indent things
    print('Is 6')  # not
    print('Is still 6')  # not
    print('Third 6')  # not
print('Afterwards 6')  # this return running normally
print()

# indentation
# increase indent, indent after an if statement or for statement (after:)
# maintain indent to indicate the scope of the block (wich lines are affected
# by the if/for)
# reduce indent back to the level of the if statement or for statement to indicate
# the end of the block
# blank lines are ignored - they do not affect indentation
# comments on a line by themselves are ignored with regard to indentation

# warning: TURN OFF TABS (ignore for .py programs)
# most text editors can turn tabs into spaces - make sure to enable this feature
# python cares a *lot* about how far a line is indented. If you mix tabs and spaces
# you may get "indentation errors" even if everything looks fine
# 4 spaces for indent, 8 spaces for 2 indents

# increase / maintain after if or for
# decrease to indicate end of block

# x = 5
# if x > 2
# -> print('Bigger than 2')  # indent
# -> print('Still bigger')  # indent
# print ('Done with 2)
# for i in range(5):
# -> print(i)  # indent
# -> if i > 2: # indent
# -> -> print('Bigger than 2')  # 2 indents
# -> print('Done with i', i) # indent
# print('All done)

# nested decisions
x = 42
if x > 1:  # if yes, then read the indendation, if not, continue the code
    print('More than 1')
    if x < 100:  # if yes, then read the indendation, if not, continue the code
        print('Less than 100')
print('All done')

# two-way decisions
# sometimes we want to do one thing if a logical expression if true and
# something else if the expression is false
# it is like a fork in the road - we must choose one or the other path but not both

x = 4
if x > 2: # if it is true, print indent, if not, print else
    print('Bigger')
else: # everything that is not True on the last "if" statement
    print('Smaller')

print('All done')