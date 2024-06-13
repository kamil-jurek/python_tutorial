# Numbers
# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). (It also supports complex numbers, which will not be explained in this tutorial).
myint = 7
print(myint)

# To define a floating point number, you may use one of the following notations:
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings are defined either with a single quote or a double quotes.
mystring = "hello"
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

########################################################
one = 1
two = 2
three = one + two
print(three)

########################################################
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

########################################################
a, b = 3, 4
print(a, b)

# Mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

# print(one + two + hello)


### EXCERCISE
print("### EXCERCISE")

# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
