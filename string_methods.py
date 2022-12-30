# Video
# https://www.youtube.com/watch?v=Bv7CAxVOONs&t=16s&ab_channel=Udacity

# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
# In this video you were introduced to methods. Methods are like some of the functions you have already seen:
# 
# len("this")
# type(12)
# print("Hello world")
# These three above are functions - notice they use parentheses, and accept one or more arguments

# A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation
# Methods are specific to the data type for a particular variable. So there are some built-in methods that are available for all strings, 
# different methods that are available for all integers, etc.

my_string = "prakash loganathan"
print(my_string.islower())
print("")

print(my_string.count('a'))
print("")

print(my_string.find('a'))
print("")
# You can see that the count and find methods both take another argument. 
# However, the .islower() method does not accept another argument.

# One important string method: format()
# We will be using the format() string method a good bit in our future work in Python
print("format() string method")
print("Prakash has {} balloons".format(27))
print("")

animal = "dog"
action = "bite"
print("Does your {} {}".format(animal, action))
print("Does your {0} {1}".format(animal, action))
print("")
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))
print("")

# Another important string method: split()
# A helpful string method when working with strings is the .split method. 
# This function or method returns a data container called a list that contains the words from the input string.

# The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". 
# It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). 
# If the sep argument is not provided, the default separator is whitespace.
# the maxsplit argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list

#split([sep, maxsplit])
print("A basic split method:")
new_str = "The cow jumped over the moon."
print(new_str.split())
print("Here the separator is space, and the maxsplit argument is set to 3.")
print(new_str.split(' ', 3))
print("Using '.' or period as a separator.")
print(new_str.split('.'))
print("Using no separators but having a maxsplit argument of 3.")
print(new_str.split(None, 3))