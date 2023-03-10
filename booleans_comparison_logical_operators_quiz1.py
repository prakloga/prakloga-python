# Quiz: Which is denser, Rio or San Francisco?
# Try comparison operators in this quiz! This code calculates the population densities of Rio de Janeiro and San Francisco.
# 
# Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
san_francisco_pop_density = sf_population/sf_area
print(san_francisco_pop_density)

rio_population, rio_area = 6453682, 486.5
rio_de_janeiro_pop_density = rio_population/rio_area
print(rio_de_janeiro_pop_density)

#Which is denser, Rio or San Francisco?
print(san_francisco_pop_density > rio_de_janeiro_pop_density)