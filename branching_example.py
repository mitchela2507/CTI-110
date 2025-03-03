# Creste a variable called senior
senior = False

# Get the age from the user
age = int(input("Enter your age: "))

# Boolean-True or False
# == is equal to
# != not equal to
# > (Greater Than), < (Less Than)
# >= Greater Than or equal to
# <= Less Than or Equal to

# if/else statement
if age >= 65: 
    print(f"You are a senior citizen who is {age} years old")   
    senior = True
elif age < 65 and age >= 18:
    print(f"You are an adult who is {age} years old")
elif age < 18 and age >= 0:
    print(f"You are a minor who is {age} years old")
else:
    print(f"{age} is not a valid age")

if senior == True:
    discount = 1.00
else:
    discount = 0

print(f"At age {age}, your discount is ${discount:.2f}")    



