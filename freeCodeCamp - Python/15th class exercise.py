# write a program to read through a file and print the contents
# of the file (line by line) all in upper case.
# the file can be any file that is .txt

# file_name = input('Enter the file name: ')
file_name = input('Enter file name: ')
file_handle = open(file_name, 'r')

for line in file_handle:
    print(line.upper().rstrip())

