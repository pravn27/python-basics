# Variable are box, which can hold values & change dynamically
x = 2
y = 3
print(x + y)
x = 10
print(x + y)
name = "python"
print(name)
# string char access [] start from 0 on left side & -1 from right side index
print(name[0])
print(name[-1])
# Substring - string index & slice string[start : stop : steps]
print(name[0:5:2])
print(name[1:])
# String char updates is immutable, not able to change
# name[0] = 'ww'
# to get length of string, use len() method
print(len(name))

# Python is dynamic datatypes
name = 12
name = "python 3x"

# To reverse a string
print(name[::-1])