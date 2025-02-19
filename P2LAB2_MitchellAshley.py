# Ashley Mitchell
# 2/19/2025
# P2LAB2
# Work with dictionaries

# Create a dictionary named cars that represents cars and their mph
cars = {"Camaro" : 18.21,   "Prius" : 53.36, "Model S" : 110, "Silverado" : 26}

#Create a list of the keys in the dictionary
keys = cars.keys()

# View the contents of the keys list
print(keys)
print("Choose a car from the list: ")
print()
for i in keys:
    print(i)
    
print()

# Get one of the keys from the user
user_input = input("Enter a vehicle to see it's mpg: ")
print()

# With user_input holding the key, we want back the value
print(f"The {user_input} gets {cars[user_input]} mpg.")
print()

# Get number of mile to drive from the user
miles = float(input(f"How many miles will you drive the {user_input}? "))
print()

# Calculate amount of gas needed to drive the chosen car the given number of miles
num_gallons = miles/cars[user_input]

print(f"{num_gallons:.2f} gallon(s) of gas are needed to drive the {user_input} {miles} miles.")

