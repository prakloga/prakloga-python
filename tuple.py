# Video
# https://www.youtube.com/watch?v=dM0UkbGAark&t=49s&ab_channel=Udacity

# Tuple: A data type for immutable ordered sequences of elements
# Tuples: A tuple is another useful container. It's a data type for immutable ordered sequences of elements. 
# They are often used to store related pieces of information.

# An ordered collection of objects which can be accessed by their indices.
# tuples are immutable - you can't add and remove items from tuples, or sort them in place.
AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))
print("AngkorWat is at latitude: {}".format(AngkorWat[0]))
print("AngkorWat is at longitude: {}".format(AngkorWat[1]))
print("")

# The parentheses are optional when defining tuples
dimensions = 52, 40, 100
# OR
# dimensions = (52, 40, 100)
print(type(dimensions))
length, width, height = dimensions # Tuple unpacking
print("The dimensions are {}x{}x{}".format(length, width, height))
print("")

# Quiz1: What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
tuple_a = 1, 2
tuple_b = (1, 2)
print(tuple_a == tuple_b)
print(tuple_a[1])
print(2 in tuple_a)