# Video
# https://www.youtube.com/watch?v=oZJdRjVLCZw&ab_channel=Udacity

# Dictionaries
# A dictionary is a mutable data type that stores mappings of unique keys to values.
print("dictionary that stores elements and their atomic numbers")
elements = {"hydrogen":1, "helium":2, "carbon": 6}
# Dictionaries can have keys of any immutable type, like integers or tuples, not just strings.
# It's not even necessary for every key to have the same type
print(elements["helium"])
print("insert 'lithium' with a value of 3 into the dictionary")
elements["lithium"] = 3
print(elements)

# We can check whether a value is in a dictionar using IN keyword
print('carbon' in elements)
print(elements.get("dilithium"))
print(elements.get("dilithium",'Does not exists'))
print("")

# Identity Operators
# is - evaluates if both sides have the same identity
# is not - evaluates if both sides have different identities

# You can check if a key returned None with the is operator. You can check for the opposite using is not.
n = elements.get("dilithium")
print(n is None)
print(n is not None)

# When to use Dictionaries?
# A dictionary will work well here as there is a key: value association. 
# In other words, there is a linkage between each holding and the information (e.g., rate of return), 
# and it can be organized under one index fund, VINIX.
VINIX =  {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85, 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 'INTC': 1.0, 'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05, 'CVX': 1.05, 'BAC': 1.15, 'JNJ': 1.41, 'GOOGL': 1.46, 'GOOG': 1.47, 'BRK.B': 1.5, 'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02, 'AMZN': 2.96, 'MSFT': 3.28, 'AAPL': 3.94}

# You can add even other details, such as rate of return YTD. 
# For that we can add the details into the value associated with the key, i.e., the ticker symbol for the holding.
VINIX = {'C': [0.74, -6.51],  'MA': [0.78, 34.77],  'BA': [0.79, 17.01],  'PG': [0.85, -8.81],  'CSCO': [0.88, 18.56],  'VZ': [0.9, 2.16],  'PFE': [0.92, 13.96],  'HD': [0.97, 3.2],  'INTC': [1.0, 2.61],  'T': [1.01, -15.19],  'V': [1.02, 24.0],  'UNH': [1.02, 19.32],  'WFC': [1.05, -3.59],  'CVX': [1.05, -5.77],  'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],  'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}

