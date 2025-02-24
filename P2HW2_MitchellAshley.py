# Ashley Mitchell
# 2/24/2025
# P2HW2
# Use lists to capture student grades

# Get 6 grades from the user - they should be floats
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Create an empty list
grades_list = []

#Use the append method to add all grades into the list
# Code looks like this: list_name.append(what_to_add_to_list)

grades_list.append(mod1)
grades_list.append(mod2)
grades_list.append(mod3)
grades_list.append(mod4)
grades_list.append(mod5)
grades_list.append(mod6)
print()

# Display the list
print(grades_list)
print()

# Display values to user
print("------------Results------------")
print(f"{'Lowest Grade:':<20} {min(grades_list)}")
print(f"{'Highest Grade:':<20} {max(grades_list)}")
print(f"{'Sum of Grades:':<20} {sum(grades_list)}")
average = sum(grades_list) / len(grades_list)
print(f"{'Average:':<20} {average:.2f}")
print("----------------------------------------")