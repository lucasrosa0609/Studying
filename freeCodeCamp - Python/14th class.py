# reading files

# its time to go find some data to mess with
# file processing
# a text file can be thought of as a sequence of lines

# using open()
# handle = open(filename, mode)
# returns a handle use to manipulate the file
# filename is a string
# mode is optional and should be 'r' if we are planning to
# read the file and 'w' if we are going to write the file

# fhand = open('mbox.txt')
# print(fhand)

# the newline character
# we use a special character called the "newline" to indicate when
# a line ends. We represent it as \n in strings
# newline is still one character not two

stuff = 'Hello\nWorld!'
print(stuff)
stuff1 = 'X\nY'
print(stuff1)
print(len(stuff1))
print()

# reading files in python