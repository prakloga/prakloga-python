'''
Practice: Quick Brown Fox
Use a for loop to take a list and print each element of the list in its own line.

Example:
'''
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for item in sentence:
    print(item)

# OR

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

'''
Practice: Multiples of 5
Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.

This should output:
5
10
15
20
25
30
'''
print("")
for i in range(5,35,5):
    print(i)

'''
Quiz: Create Usernames
Write a for loop that iterates over the names list to create a usernames list. 
To create a username for each name, make everything lowercase and replace spaces with underscores. 
Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this Stack Overflow answer.

https://stackoverflow.com/questions/12723751/replacing-instances-of-a-character-in-a-string/12723785#12723785
'''
print("")
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#print(names)
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ','_'))
print(usernames)

'''
Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. 
What would this do?
'''
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

'''
Quiz: Modify Usernames with Range
Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
'''
print("")
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].replace(' ','_').lower()

print(usernames)

'''
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. 
You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.
'''
print("")
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)

'''
Quiz: Create an HTML List
Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. 
For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. 
Following that is one line per element in the source list, surrounded by <li> and </li> tags. 
The final line of the string should be the closing tag </ul>.
'''
print("")
items = ['first string', 'second string']
print('<ur>')
for item in items:
    print('<li>{}</li>'.format(item))
print('</ul>')

# OR
print("")
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
for item in items:
    html_str += '<li>{}</li>\n'.format(item)
html_str += '</ul>'
print(html_str)

'''
Test Your Loop Knowledge
In case you want to test any code for the quizzes that follow, 
there is a code editor at the bottom of this page where you can experiment.
'''
# range(start, stop, step)
print(list(range(4))) # stop
print(list(range(4,8))) # start, Stop
print(list(range(4,10,2))) # start, stop, step
print(list(range(0,-5))) #start, stop
print(list(range(0,-5, -1)))

#Use the code below to complete the next quiz.

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())
print(lower_colors)
