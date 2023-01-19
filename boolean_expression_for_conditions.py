# Video
# https://www.youtube.com/watch?v=gWmIKWgzFqI&t=103s&ab_channel=Udacity
# https://www.youtube.com/watch?v=95oLh3WtdhY&t=13s&ab_channel=Udacity
# https://www.youtube.com/watch?v=e52uw7ejV8k&t=3s&ab_channel=Udacity

# Example1:
weight = 164
height = 38
#print((weight / height)**2)

if 18.5 <= ((weight / height)**2) < 25:
    print("BMI is considered 'Normal'")

# Example2:
print("")
is_raining = True
is_sunny = True

if is_raining and is_sunny:
    print("Is there a rainbow?")

# Example3
print("")
unsubscribed = False
location = 'USA'

if (not unsubscribed) and (location == 'USA' or location == 'CA'):
    print("send email")
else:
    print("Don't send email")

# Good and Bad Examples
'''
Lessons Learned
- Don't use if True: | if False
- Be careful writing expressions that use logical operators
and | or | not
- Do not evaluate the truth of a boolean variable with == 
The variable itself is a boolean expression
'''
# Bad example: 1
print("")
if True:
    print("This indented code will always get run")

# Bad example: 2
is_cold = False

if is_cold or not is_cold:
    print("The weather is cold or not cold")

# Bad example: 2
weather = "snow"
if weather == "snow" or "rain":
    print("Wear boots")

# Correct way to write is
weather = "snow"
if weather == "snow" or weather == "rain":
    print("Wear boots")

# Good Example:
is_cold = True
if is_cold:
    print("The weather is cold")

correct_answer = False
if not correct_answer:
    print("This is incorrect - try again")

# Truth Value Testing
'''
If we use a non-boolean object as a condition in an if statement in place of the boolean expression, Python will check for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered False in Python:

constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)
'''
errors = 3
if errors:
    print("You have {} error to fix".format(errors))
else:
    print("No errors to fix")
# In this code, errors has the truth value True because it's a non-zero number, so the error message is printed. 






