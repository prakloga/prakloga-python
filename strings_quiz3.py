# Quiz: len()
# Use string concatenation and the len() function to find the length of a certain movie star's actual full name.
# Store that length in the name_length variable. 
# Don't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = given_name+' '+middle_names+' '+family_name
name_length = len(full_name)
print(name_length)

# OR
name_length = len(given_name) + len(middle_names) + len(family_name) + 2
print(name_length)