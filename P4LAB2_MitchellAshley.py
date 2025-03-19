# Ashley Mitchell
# 3/19/2025
# P4LAB2
# Using a for lopp insode a while lopp to print math

# Create the variable to control while loop
run_again = "yes"

# While loop that controls the whole program
while run_again != "no":
    # Get it from user
    user_num = int(input("Enter an integer: "))
    if user_num < 0:
        print("This program does not handle neagtive number")
    else: # user_num is 0 or greater
        for i in range(1,13):
            print(f"{user_num} * {i} = {user_num*i}")
    run_again = input(" Would you like to run the program again? 'yes'/'no': ")
# While loop ends here
print("Exiting program...")


