# Quiz: List Indexing
# Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. 
# For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
# 
# Remember to account for zero-based indexing!
month = 8
#month_name     [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
days_in_month = [31,  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31]
num_days = days_in_month[month - 1]
print(num_days)

# Quiz: Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
print(eclipse_dates[-3:])
print("")

# Suppose we have the following two expressions, sentence1 and sentence2:
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
# Match the Python code below with the value of the modified sentence1 or sentence2. 
# If the code results in an error, match it with “Error”.#
print('sentence2[6]="!"')
sentence2[6]="!"
print(sentence2)
print("")

sentence2[0]= 'Our mejesty'
print(sentence2)
print("")

# sentence1[30] = '!' # TypeError: 'str' object does not support item assignment
sentence2[0:2] = ["We", "want"]
print(sentence2)
print("")