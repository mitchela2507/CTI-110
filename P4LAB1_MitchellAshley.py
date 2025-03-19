# Ashley Mitchell
# 3/19/2025
# P4LAB1
# Turtle graphics progarm to draw triangle and square

import turtle
win = turtle.Screen()
win.bgcolor('medium blue')
tom = turtle.Turtle()

# Set the way turtle looks
tom.pensize(6)
tom.pencolor('light green')
tom.shape('arrow')

# Test
# tom.forward(100)

# for loop that runs 4 times
for i in range(4):
    tom.forward(100)
    tom.right(90)
    
# while loop that rins 3 times
this_run = 0

while this_run < 3:
    tom.forward(100)
    tom.left(120)
    this_run += 1

# Keeps the window open after shape is drawn
win.mainloop()