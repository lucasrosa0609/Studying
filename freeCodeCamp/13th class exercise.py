# take the following python code that stores a string
# str = 'X-DSPAM-Condifence: 0.8475'
# use find and string slicing to extract the position of the string after the colon
# character and then use the float function to convert the extracted string into
# a floating point number

data = 'X-DSPAM-Condifence: 0.8475'
colon = data.find(':')
print(colon)
extract = data[18+1: -1]
extract = float(extract)
print(extract)
print(type(extract))
print(extract * 3)
