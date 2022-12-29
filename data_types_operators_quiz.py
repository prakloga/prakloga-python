# What type does this object have? "12". There is a coding environment further down this page that you can use for experimentation.
print("Quiz1")
print(type("12"))
print("")

# What type does this object have? 12.3 There is a coding environment further down this page that you can use for experimentation.
print("Quiz2")
print(type(12.3))
print("")

# What type does this object have? len("my_string") There is a coding environment further down this page that you can use for experimentation.
print("Quiz3")
print(type(len("my_string")))
print("")

# What type does this object have? "hippo" *12 There is a coding environment further down this page that you can use for experimentation.
print("Quiz4")
print(type("hippo" *12))
print("")

# Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.
# 
# Calculate and print the total sales for the week from the data provided. 
# Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. 
# You’ll need to change the type of the input data in order to calculate that total.
print("Quiz: Total Sales")
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
week_sale = (int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales))
#print(week_sale)
print("This week's total sales: "+str(week_sale))

# OR
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)