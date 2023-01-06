# Video
# https://www.youtube.com/watch?v=1EOp1AaP3BE&t=1s&ab_channel=Udacity

# Compound Data Structures
# We can include containers in other containers to create compound data structures. 
# For example, this dictionary maps keys to values that are also dictionaries!
elements = {"hydrogen": {"number":1, "weight":1.0074, "symbol":'H'}
           ,"helium": {"number": 2, "weight": 4.002602, "symbol": "He"}
           }
#We can access elements in this nested dictionary like this.
print("get the helium dictionary")
print(elements["hydrogen"])
print("get hydrogen's weight")
print(elements["hydrogen"]["weight"])
print("")

# You can also add a new key to the element dictionary.
oxygen = {"number":8, "weight":15.99, "symbol":"O"}
elements["oxygen"] = oxygen
print(elements)
print("")

# Quiz: Adding Values to Nested Dictionaries
# Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. 
# After inserting the new entries you should be able to perform these lookups:
#
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements["hydrogen"]["is_noble_gas"] = False
elements["helium"]["is_noble_gas"] = True
elements["oxygen"]["is_noble_gas"] = True
print(elements)
print(elements["hydrogen"]["is_noble_gas"])
print(elements["helium"]["is_noble_gas"])

# Quiz2: Collections
# Check the attributes of a collection for which using a Python list would be appropriate.
# 1.Items are always indexed with numbers starting at 0
# 2.Sortable
# 3.Add items with .append

# Quiz3
# Check the attributes of a collection for which using a Python set would be appropriate.
# 1. Order in which items appear can be inconsistent
# 2. Mutable (you can change it)
# 3. Add items with .add

# Quiz4
# Check the attributes of a collection for which using a Python dictionary would be appropriate.
# 1. Each item contains two parts
# 2. Order in which items appear can be inconsistent
# 3. Can be nested


