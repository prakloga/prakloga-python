# Quiz: Count Unique Words
# Your task for this quiz is to find the number of unique words in the text. 
# In the code editor below, complete these three steps to get your answer.
# 
# Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
# Convert the list into a data structure that would keep only the unique elements from the list.
# Print the length of the container.
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')
# split verse into list of words
verse_list = verse.split()
print(verse_list, "\n")
verse_set = set(verse_list)
print(verse_set, "\n")
print(len(verse_set))

# OR 
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)

# Quiz: Verse Dictionary
# In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys and the number of times they appear in verse stored as values. 
# Use this dictionary to answer the following questions. Submit these answers in the quiz below the code editor.
# 
# Try to answer these using code, rather than inspecting the dictionary manually!
# 
# How many unique words are in verse_dict?
# Is the key "breathe" in verse_dict?
# What is the first element in the list created when verse_dict is sorted by keys?
# Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. 
# Use this list of keys to answer the next two questions as well.
# Which key (word) has the highest value in verse_dict?
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# How many unique words are in verse_dict?
num_keys = len(verse_dict)
print(num_keys)

# Is the key "breathe" in verse_dict?
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# What is the first element in the list created when verse_dict is sorted by keys?
# Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. 
# Use this list of keys to answer the next two questions as well.
verse_dict_keys = verse_dict.keys()
print(sorted(verse_dict_keys))

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])

# In this lesson, we covered four important data structures in Python:
# 
# Data Structure	Ordered	Mutable	Constructor	Example
# List	            Yes	    Yes	    [ ] or list()	[5.7, 4, 'yes', 5.7]
# Tuple	            Yes	    No	    ( ) or tuple()	(5.7, 4, 'yes', 5.7)
# Set	            No	    Yes 	{}* or set()	{5.7, 4, 'yes'}
# Dictionary	    No	    No**	{ } or dict()	{'Jun': 75, 'Jul': 89}
# * You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. 
# So to create an empty set, use set().
# ** A dictionary itself is mutable, but each of its individual keys must be immutable.


