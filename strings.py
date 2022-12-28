# Video
# https://www.youtube.com/watch?v=ySZDrs-nNqg&t=83s&ab_channel=Udacity

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"

this_string = 'Simon\'s skateboard is in the garage.'
#this_string = 'Simon's skateboard is in the garage.'
this_string = "Simon's skateboard is in the garage."
print(this_string)

# + : Combine strings
first_word = "Hello"
second_word = "There"
print(first_word + ' '+ second_word)

# * : Repeat strings
print(first_word * 5)

# / : unsupported operand type(s) for /: 'str' and 'str'
# print(first_word / second_word)

# Index operation for String
# Python uses 0 indexing
print(first_word[0])

# The len() function
# len() is a built-in Python function that returns the length of an object, like a string. 
# The length of a string is the number of characters in the string. 
print(len("ababa")/len("ab"))
udacity_length = len("Udacity")
print(udacity_length)

# We’ve already seen that the type of objects will affect how operators work on them. What will be the output of this code?
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)




