# Video
# https://www.youtube.com/watch?v=jWiIUMrwPqA&t=123s&ab_channel=Udacity
# https://www.youtube.com/watch?v=KZubH5XT0eU&t=133s&ab_channel=Udacity
# https://www.youtube.com/watch?v=G8qUNOTHtrM&t=52s&ab_channel=Udacity

# IF Statement
# An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. 
# Here's a simple example.
phone_balance = 3
bank_balance = 100
print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print("After IF statement")
print(phone_balance, bank_balance,"\n")

# Use Comparison Operators in Conditional Statements
# If, Elif, Else
# In addition to the if clause, there are two other optional clauses often used with an if statement. For example:
n = 3
if n % 2 == 0:
    print("Number "+str(n)+" is even.")
else:
    print("Number "+str(n)+" is odd." )
print("\n")

# Example: 2
season = 'summer'

if season == 'spring':
    print('Plant the garden!')
elif season == 'summer':
    print('Water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('Stay indoor!')
else:
    print('Unrecognized season')
print("")

# Example: 3
# Here are the age limit for the bus fair
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
# These line determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50
# Here is the logic for bus fair price
age = 68

if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old pay ${} to ride the bus.".format(age, ticket_price)
print(message, "\n")
 
