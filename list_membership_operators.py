# Video
# https://www.youtube.com/watch?v=Tg58Z58m2Lo&t=1s&ab_channel=Udacity
# https://www.youtube.com/watch?v=f4OF9XtXUR8&ab_channel=Udacity
# https://www.youtube.com/watch?v=dVsJ9yzbSHE&ab_channel=Udacity

# Lists: Data type for MUTABLE and ORDERED sequence of elements
# Data structures are containers that organize and group data types together in different ways. 
# months = [0,        1,         2,       3,       4,     5,      6,      7,        8,           9,         10,         11]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[0])
print(months[1])
print(months[7])
print(months[-1]) # December
#print(months[25]) # IndexError: list index out of range
print("")

# You saw here that you can create a list with square brackets. 
# Lists can contain any mix and match of the data types you have seen so far.
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
print(len(list_of_random_things)) #4
#print(list_of_random_things[len(list_of_random_things)]) #IndexError: list index out of range
print(list_of_random_things[len(list_of_random_things)-1])
print(list_of_random_things[-1])
print(list_of_random_things[-2])

print("")
q3 = months[6:9]
print(q3)
print("")

first_half = months[:6]
print(first_half)
print("")

second_half = months[6:]
print(second_half)
print("")

print("There are {} months".format(len(months)))
print("")

# Slice and Dice with Lists
# You saw that we can pull more than one value from a list at a time by using slicing. When using slicing, 
# it is important to remember that the lower index is inclusive and the upper index is exclusive.
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[1:2])
print(list_of_random_things[:2])
print(list_of_random_things[1:])
print("")

# Membership Operator[IN or NOT IN]
# Are you in OR not in?
# You saw that we can also use in and not in to return a bool of whether an element exists within our list,
# or if one string is a substring of another.
print('this' in 'this is a string')
print('in' in 'this is a string')
print(5 in [1, 2, 3, 4, 6])
print(5 not in [1, 2, 3, 4, 6])
print('January' in months)

# Mutability: is about whether or not we can change an object once it has been created.
# However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.
# Order: is about whether the position of an element in the object can be used to access the element.
print("")
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'One'
print(my_lst)
# As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are mutable
greeting = "Hello there"
# greeting[0] = 'M' # TypeError: 'str' object does not support item assignment
# This is because strings are immutable. This means to change this string, you will need to create a completely new string.

# There are two things to keep in mind for each of the data types you are using:
# 
# Are they mutable?
# Are they ordered?

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print(VINIX[0])
print(VINIX[1])
print('GE' in VINIX)
print('GOOGL' in VINIX)


