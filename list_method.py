# Video
# https://www.youtube.com/watch?v=7QShK49tquM&t=27s&ab_channel=Udacity
# https://www.youtube.com/watch?v=ugVkJZFU3U8&ab_channel=Udacity

# The Value of Mutable and Immutable change behave differently.
# String: immutable
name = 'Jim'
student = name
name = 'Tim'
print(name)
print(student)

# List: Mutable and ordered
scores = ['B', 'C', 'A', 'D', 'B', 'A']
grades = scores
print("scores: " + str(scores))
print("grades: " + str(grades))
print("")
scores[3]='B'
print("scores: " + str(scores))
print("grades: " + str(grades))
print("")

# len() returns how many elements are in a list.
batch_sizes = [15, 6, 89, 34, 65, 35]
print(len(batch_sizes))

# max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list.
# The maximum element in a list of numbers is the largest number. 
# The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. 
# This works because the the max function is defined in terms of the greater than comparison operator. 
# The max function is undefined for lists that contain elements from different, incomparable types.
print(max(batch_sizes))

# min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
print(min(batch_sizes))

# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.
print(batch_sizes)
print(sorted(batch_sizes))
print(sorted(batch_sizes, reverse = True))
print("")

# Useful Functions for Lists II
# join method
# Join is a string method that takes a list of strings as an argument,
# and returns a string consisting of the list elements joined by a separator string.

#  "\n" as the separator so that there is a newline between each element.
new_str = '\n'.join(["fore", "aft", "starboard", "port"])
print(new_str)
print("")

name = "-".join(["García", "O'Kelly"])
print(name)

# This will produce unexpected result because the list values are not seperated by comma(,)
name = "-".join(["García" "O'Kelly"])
print(name)

# Join method does not work for mixed data type value in LIST
# TypeError: sequence item 1: expected str instance, int found
stuff = ["Thing", 42, "nope"]
#print(" and ".join(stuff))
print("")

# append method
# A helpful method called append adds an element to the end of a list.
python_varities = ["Burmese Python", "African Rock Python", "Ball Python", "Reticulated Python", "Angolan Python"]
python_varities.append("Blood Python")
print(python_varities)

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
letters.pop()
print(letters)
