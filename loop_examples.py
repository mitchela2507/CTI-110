# Learning about loops - execute code multiple times

# for loop - execute a predetermined number of times

'''
range function can be used with 1, 2 or 3 parameters
range(5) --> 0,1,2,3,4
range(3,10) --> 3,4,5,6,7,8,9
range(0,13,3) --> 0,3,6,9,12

syntax is range(start, stop, increment) - stop value is NON-inclusive
'''

# Make a loop that executes 5 times
for value in range(0,11,2):
    #print("Life is good :) " + str(value))
    print(value)


print()
for banana in range(0,9):
    print(banana + 1)

print()
# Loop through a list
friends = ["Darlene", "John", "Mandy", "Natalie", "Hana"]

amigo = "John"

'''
for character in amigo:
    print(character)
'''

for name in friends:
    if name == amigo:
        print("There is John!")
    else:
        print(f"This friend is {name}, not John!")



price_list = [1.00, 2.50, 1.50, 0.50]

print(sum(price_list))

total = 0
for each in price_list:
    total += each
    print(total)
print(f"Final Total: ${total:.2f}")


# while loop - continues executing until a specific condition is met

# user-controlled loop

# Create variable to control loop
run_again = input("Start program? ('yes'/'no'):")

while run_again != "no":
    print("Program is running....")
    run_again = input("Continue program? ('yes'/'no'):")
# while loop ends here
print("Program has ended....")
