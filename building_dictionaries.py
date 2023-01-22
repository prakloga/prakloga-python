'''
For example, we can create a dictionary, word_counter, that keeps track of the total count of each word in a string.
'''
# Method 1: Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Step 1: Create an empty dictionary.
word_counter = {}

#Step 2. Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. 
# If not, add the element to the dictionary and set its value to 1.
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] = word_counter[word]+1

print(word_counter)
print("\n")

#Method 2: Using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Step 1: Create an empty dictionary.
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word,0)+1

print(word_counter)


