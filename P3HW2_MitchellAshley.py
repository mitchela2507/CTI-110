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
'''
hours_worked =  45
pay_rate =  17.5

print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print("-----" * 20)
print(f"{hours_worked:<20}${pay_rate:<20.2f}")
