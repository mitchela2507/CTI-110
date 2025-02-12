# This program calcualtes energy in joules

print("Calculate energy based on the mass entered!!")

# Get the mass from the user
mass = float(input("Enter the mass of the object: "))

# Declare (create) the variable speed_of_light in m/s
speed_of_light = 299792458

# Calculate E for energy
energy = mass * speed_of_light ** 2

# Display results to the screen
print("The formula for energy is energy = mass * speed_of_light ** 2 and the value is", energy)
