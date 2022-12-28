# Video
# https://www.youtube.com/watch?v=MiJ1vfWp-Ts&ab_channel=Udacity
# https://www.youtube.com/watch?v=UxkIwcOczQQ&ab_channel=Udacity
# https://www.youtube.com/watch?v=UxkIwcOczQQ&ab_channel=Udacity

# Integers and Floats
# There are two Python data types that could be used for numeric values:
# int - for integer values
# float - for decimal or floating point values

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
print(x, y)
print(type(x))
print(type(y))

# Because the float, or approximation, for 0.1 is actually slightly more than 0.1, 
# when we add several of them together we can see the difference between the mathematically correct answer 
# and the one that Python creates.
print(.1 + .1 + .1 == .3)

# You should limit each line of code to 80 characters, though 99 is okay for certain use cases.
# https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width

# PEP8
# https://peps.python.org/pep-0008/
