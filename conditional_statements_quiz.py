# Practice: Which Prize
# Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.
# 
# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
# All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.
# 
# In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. 
# If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."
# 
# Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. You can hide your other inputs by commenting them out.
points = 201

if points <= 50:
    prize = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    prize = "Oh dear, no prize this time."
elif points <= 180:
    prize = "Congratulations! You won a wafer-thin mint!"
elif points <= 200:
    prize = "Congratulations! You won a penguin!"
else:
    prize = "Input takes on positive integer values up to 200"

print(prize)

# Solution - Other
points = 201

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result, "\n")


# Quiz: 2
# Quiz: Guess My Number
# You decide you want to play a game where you are hiding a number from someone. Store this number in a variable called 'answer'. 
# Another user provides a number called 'guess'. By comparing guess to answer, you inform the user if their guess is too high or too low.
# 
# Fill in the conditionals below to inform the user about how their guess compares to the answer.

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 100
guess = 120

if guess < answer:
    result = "Oops! your guess is too low"
elif guess > answer:
    result = "Ooops! your guess is too high"
elif guess == answer:
    result = "Nice! your guess match the answer"

print(result,"\n")

# Quiz: Tax Purchase
# Depending on where an individual is from we need to tax them appropriately. 
# The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
# Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.
ca_tax = 7.5/100
print("CA TAX "+str(ca_tax))
mn_tax = 9.5/100
print("MN TAX "+str(mn_tax))
ny_tax = 8.9/100
print("NY TAX "+str(ny_tax))
oh_tax = 7.5/100
print("OH TAX "+str(oh_tax))

state = 'OH'
purchase_dollar = 200

if state == 'CA':
    total = purchase_dollar*(1+ca_tax)
elif state == 'MN':
    total = purchase_dollar*(1+mn_tax)
elif state == 'NY':
    total = purchase_dollar*(1+ny_tax)
elif state == 'OH':
    total = purchase_dollar*(1+oh_tax)

print(total, "\n")

# Solution: Tax Purchase
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


