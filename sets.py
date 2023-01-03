# Video
# https://www.youtube.com/watch?v=lrrwBc-DSDo&t=43s&ab_channel=Udacity

# Sets: Mutable & Unordered
# A set is a data type for mutable unordered collections of unique elements. 
# One application of a set is to quickly remove duplicates from a list.

countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana']
print(len(countries))
countries_set = set(countries)
print(countries_set)
print(len(countries_set))
print("")

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
print("")

# Sets support the IN operator the same as lists do. 
fruits = {'apple', 'orange', 'banana', 'grapefruit'}
print('watermelon' in fruits)
print('green apple' not in fruits)

# You can add elements to sets using the ADD() method
fruits.add('watermelon')
print(fruits)

# remove elements using the POP() method
# when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".
fruits.pop()
print(fruits)
# Methods like union, intersection, and difference are easy to perform with sets, 
# and are much faster than such operators with other containers.

# QUIZ-1
# What would the output of the following code be?
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(a)
b = set(a)
print(b)
print(len(a) - len(b))

# Quiz-2: add and pop
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(b)
b.add(5)
print(b)
b.pop()
print(b)