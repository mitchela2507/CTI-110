# Ashley Mitchell
# 3/26/2025
# P4HW2
# Determine employee's regular pay, OT pay, and gross pay while using loops

# Create the accumlator variables
total_num_emp = 0
total_OT_pay = 0
total_reg_pay = 0
gross_pay = 0

# create outer loop that runs until user inputs "Done"
emp_name = input("Enter employee's name or 'Done' to terminate: ")
while emp_name.lower() != "done":
    hours_worked = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))

    # Code to caluclate the values

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

    emp_name = input("Enter employee's name or 'Done' to terminate: ")
# Loop has broken, display final accumlated totals below
print()
print()
print(f"Total number of employees entered: {emp_name}")
print(f"Total amount pad for overtime: ${total_OT_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_reg_pay:.2f}")
print(f"Total amount paid in gross: ${gross_pay:.2f}")