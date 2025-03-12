# Ashley Mitchell
# 3/10/2025
# P3HW2
# Determine employee's regular pay, OT pay, and gross pay

'''
Pseudocode:

Get employye name from user (use input function)
Get hours worked from user (use input and float function)
Get employee pay rate from user (use input and float function)

Calculate values:

# Overtime is worked
if hours_worked > 40: 
    Calculate OT_hours (hours_worked - 40)
    Calculate OT_pay_rate (pay_rate * 1.5)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to 40 (Create a variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross_pay (OT_pay + reg_pay)

# No Overtime is worked
else:  
    OT_hours is zero (Create a variable)
    OT_pay_rate is zero (Create a variable)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to hours_worked (Create a variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross_pay (OT_pay + reg_pay)

Display all values with width formatting

hours_worked =  45
pay_rate =  17.5

print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print("-----" * 20)
print(f"{hours_worked:<20}${pay_rate:<20.2f}")
'''

# Get employye name from user (use input function)
emp_name = input("Enter employee's name: ")

# Get hours worked from user (use input and float function)
hours_worked = float(input("Enter number of hours worked: "))

# Get employee pay rate from user (use input and float function)
pay_rate = float(input("Enter employes's pay rate: "))


# Overtime is worked
if hours_worked > 40: 
    OT_hours = hours_worked - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT_hours * OT_pay_rate
    reg_hours =  40
    reg_pay = reg_hours * pay_rate
    gross_pay = OT_pay + reg_pay

# No Overtime is worked
else:
    OT_hours = 0
    OT_pay_rate = 0
    OT_pay = OT_hours * OT_pay_rate
    reg_hours = hours_worked
    reg_pay = reg_hours * pay_rate
    gross_pay = OT_pay + reg_pay

# Display all values with width formatting
print("--" * 20)
print(f"{'Employee Name:':<15} {emp_name}")

print()

print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-----" * 23)
print(f"{hours_worked:<20.1f}{pay_rate:<20.1f}{OT_hours:<20.1f}{OT_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:<20.2f}")
