# Video
# https://www.youtube.com/watch?v=yN6Fam_vZrU&t=72s&ab_channel=Udacity

# Type conversion
count = int(4.0)
print(count)
print(type(count))
print("")

grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))
print("")

house_number = 13
street_name = "The Crescent"
town_home = "Belmont"
print(type(house_number))
address = str(house_number) + ' '+ street_name+' '+town_home
print(address)
print("")

# Type and Type Conversion
# You have seen four data types so far:
# 
# int
# float
# bool
# string
# You got a quick look at type() from an earlier video, and 
# it can be used to check the data type of any variable you are working with.
print(type(633))
print(type(633.0))
print(type('633'))
print(type(True))
print("")

print("0" + "5")
print(0 + 5)
# print("0" + 5) #TypeError: can only concatenate str (not "int") to str

