# In-class practice Module 4 - formatting output

# Get an amount of money from the user (input)
item = input("What item are you purchasing? ")
money = float(input("Enter an amout of money with change: "))

# The plus sign is concantenation of strings, not addition
print("The amount entered: $" + str(money))
print()
# Use a formatted string to print a specific amount of places after decimal
# .upper()=uppercase in string (ex: {item.upper()}=dog food to DOG FOOD)
print(f"The amount entered is ${money:.2f} and the item is {item}")

# This is a formatted string
print(f"I am buying a {item} and it costs ${money:.2f}")
print()
#This is a non-formatted string
print("I am buying a",item, "and it costs $" + str(money))