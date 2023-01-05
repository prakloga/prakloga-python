# Quiz: Define a Dictionary
# Define a dictionary named population that contains this data:
# 
# Keys	Values
# Shanghai	17.8
# Istanbul	13.3
# Karachi	13.0
# Mumbai	12.5

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.
population = {"Shanghai":17.8 ,"Istanbul":13.3 ,"Karachi":13.0 ,"Mumbai":12.5}
print(type(population))

# Quiz:2
# Which of these could be used as the key for a dictionary? (Choose all that apply.) 
# Hint: Dictionary keys must be immutable, that is, they must be of a type that is not modifiable.
# Answer: String, Integer, Float, Tuple

# Quiz:3
# What happens if we look up a value that isn't in the dictionary? 
# Create a test dictionary and use the square brackets to look up a value that you haven't defined. What happens?
test_dict = {"one":1, "two":2, "three":3, "four":4}
# print(test_dict["five"]) # KeyError: 'five'

# Quiz:4
# get with a Default Value
# Dictionaries have a related method that's also useful, get(). 
# get() looks up values in a dictionary, but unlike looking up values with square brackets, 
# get() returns None (or a default value of your choice) if the key isn't found. 
# If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.
elements = {"hydrogen":1, "helium":2, "carbon": 6}
print(elements.get('dilithium'))
# print(elements['dilithium'])
print(elements.get('kryptonite','There\'s no such element!'))
print("")

# Quiz:5
# Checking for Equality vs. Identity: == vs. is
# What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

# Quiz: 6
# Context
# Use the dictionary below to answer ALL of the questions regarding dictionaries. 
# Consider you have a dictionary named animals that looks like this:
animals = {'dogs': [20, 10, 15, 8, 32, 15]
         , 'cats': [3,4,2,8,2,4]
         , 'rabbits': [2, 3, 3]
         , 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
# Let's try a few ideas with this dictionary! If you want to try any of the code yourself, 
# you can test it in the environment at the bottom of the page.
print("The data type of the keys in the dictionary?")
# String
print("The data type of the values in the dictionary.")
print(type(animals['dogs'])) # list
print("The result of animals['dogs'].")
print(animals['dogs'])
print("The result of animals['dogs'][3].")
print(animals['dogs'][3])
print("The result of animals[3]")
#print(animals[3]) #KeyError: 3
print("The result of animals['fish']")
print(animals['fish'])



