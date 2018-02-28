#####
# This is the Strings tutorial
#####
title = "Strings Tutorial"
print(title)

##
string = "Example"
print(string)

# escaping
string = "I'm going"
print(string)

string = "I\"m going"
print(string)

# Multi-line
string = "first line\nSecond line"
print(string)

# Functions
print("String functions")
string = "Python"
print(string[2])  # => 't' start left, with number 0
print(string[-1])  # => 'n' start from right

print(string[0:3])  # => 'Pyt' up to 3-1
print(string[:3])  # => 'Pyt' up to 3-1
print(string[-2:])  # => 'on' up to end
print(string[-12:])  # => 'Python' all to start

print(string[0:30])  # => 'Python' up to end
print(string[:30])  # => 'Python' up to end

# len
print(len(string))  # => 6
print(string.title())  # => 'Python'
print(string.capitalize())  # => 'Python'

paragraph = "The word the house the queen"
print(paragraph.count("the"))  # => '2' count how many instance of the word
print("center".center(20, '*'))  # => '*******center*******' center the word with optional padding
print(string.endswith("on"))  # => true, if ends with
print(string.find("on"))  # => 4, which is the position from 0
print(string.index("on"))  # => 4, similar to find but will throw Error

# formatting
print("The program is {0}".format(string))  # => The program is Python
print("The number is {:n}".format(12345.89))  # => The number is 12345.9 , uses the Locale

print("{key} is equal {value}".format_map({"key": "someKey", "value": "someValue"}))
# someKey is equal someValue, format using a supplied dictionary / map

print("a13".isalnum())  # => true
print("1113".isdigit())  # => true

print('1,2,,3,'.split(','))  # => split into an array  ['1', '2', '', '3', '']
print('1,2,,3,'.split(',', maxsplit=1))  # => split into an array  ['1', '2,,3,']

print("upper".swapcase())  # => UPPER,  toggle case
