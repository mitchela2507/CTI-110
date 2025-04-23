# Ashley Mitchell
# 3/24/2025
# P4HWl
# Using a for loop inside a while lopp to print math

'''
Create empty list to hold grades (grade_list)
num_scores = Get input form user (how many scores to enter)
(python) for score in range(num-scores):
get one score from the user-->put in variable & int/float
grade = int(input(f"Enter score #{score +1}"))
* While loop -->while grade is invalid
    while grade < 0 or grade > 100:
--> Tell user grade is invalid
    grade = int(input(Enter score #{score +1} again: ))
# Add grade to grades_list
min(grades_list)
remove min from list
'''

num_scores = int(input("How many scores do yo want to enter? "))

# Create empty list to hold grades (grade_list)
grade_list = []

for score in range (num_scores):
    grade = int(input(f"Enter score # {score + 1}: "))
    while grade < 0 or grade > 100:
        print("INVAILD Score entered!!!!")
        print("Score should be between 0 and 100")
        grade = int(input(f"Enter score # {score + 1} again: "))
    grade_list.append(grade)

print()

print("----------Results----------")

print(f"Lowest Score: {min(grade_list)}")

grade_list.remove(min(grade_list))
print(f"Modified List: {grade_list}")

avg = sum(grade_list)/len(grade_list)
print(f"Score Average: {avg:.2f}")

if avg >= 90:
    print('Grade: A')
elif avg >= 80:
    print('Grade: B')
elif avg >= 70:
    print('Grade: C')
elif avg >= 60:
    print('Grade: D')
else:
    print('Grade: F') # TO DO: finish this