# about characters and strings

# representing simples strings
# each character is represented by a number between 0 and 256 stores in
# 8 bits of memory. we refer to "8 bits of memory as "byte" of memory.
# The ord() function tells us the numeric value of a simple ASCII character

print(ord('H'))
print(ord('h'))

# multi-byte characters
# to represent the wide range of character computers must handle we represent
# characters with more than one byte
# UTF-16 - Fixed lenght - two bytes
# UTF-32 - Fixed Lenght - Four Bytes
# UTF-8 - 1-4 byter
    # upwards compatible with ASCII
    # automatic detectio9ns between ASCI and UTF-8
    # UTF - 8 is recommended practice for encoding data to be exchanged between systems

# in python 3, all strings are Unicode

# python strings to bytes
# whe nwe talk to an external resource like a network sockket we send bytes,
# so we need to encode Python 3 strings into a given character ecoding.
# When we read data from an external resource, we must decode it based on
# the character set so it is properly represented in python 3 as a string

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     mystring = data.decode()
#     print(mystring)

