# Quiz: Changing Variable Values
# How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.
# 
# We're intentionally not providing a place to execute the code here
# , because we want to help you practice the important skill of walking through lines of code by hand.
# 
# Each line of code executes in order, one at a time, with control going from one line to the next.

carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
print(crs_per_rab)

rabbits = 12
crs_per_rab = carrots/rabbits
print(crs_per_rab)
