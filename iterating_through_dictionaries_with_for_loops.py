'''
Iterating Through Dictionaries with For Loops
When you iterate through a dictionary using a for loop, doing it the normal way (for n in some_dict) will only give you access to the keys in the dictionary - which is what you'd want in some situations. 
In other cases, you'd want to iterate through both the keys and values in the dictionary. Let's see how this is done in an example. 
Consider this dictionary that uses names of actors as keys and their characters as values.
'''
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
# Iterating through it in the usual way with a for loop would give you just the keys, as shown below:
for key in cast:
    print(key)

# If you wish to iterate through both keys and values, you can use the built-in method items like this:
for key, value in cast.items(): #items is an awesome method that returns tuples of key, value pairs, 
                                #which you can use to iterate over dictionaries in for loops.
    print('Actor: {}  Role: {}'.format(key, value))

'''
Quiz: Fruit Basket - Task 1
You would like to count the number of fruits in your basket. In order to do this, you have the following dictionary and list of fruits. 
Use the dictionary and list to count the total number of fruits,but you do not want to count the other items in your basket.
'''
print("")
print("Quiz: Fruit Basket - Task 1")
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
result = 0

for key, value in basket_items.items():
    if key in fruits:
        result = result+value

print("There are {} fruits in the basket".format(result))

'''
Quiz: Fruit Basket - Task 2
If your solution is robust, you should be able to use it with any dictionary of items to count the number of fruits in the basket. 
Try the loop for each of the dictionaries below to make sure it always works.
'''
print("")
print("Quiz: Fruit Basket - Task 2")

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
   if object in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))



'''
Quiz: Fruit Basket - Task 3
So, a couple of things about the above examples:

It is a bit annoying having to copy and paste all the code to each spot - wouldn't it be nice to have a way to repeat the process without copying all the code? Don't worry! You will learn how to do this in the next lesson!

It would be nice to keep track of both the number of fruits and other items in the basket.

Use the environment below to try out this second part.
'''
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print("The Number of fruits is {}. There are {} objects that are not fruits".format(fruit_count, not_fruit_count))