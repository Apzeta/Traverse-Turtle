import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Iterate through turtle_shapes and create turtles with different shapes
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)

    # Set the pen up when creating the turtle object
    t.penup()

    # Change color: pop the color from turtle_colors list
    new_color = turtle_colors.pop()
    t.fillcolor(new_color)
    t.pencolor(new_color)

    my_turtles.append(t)

# Starting position for turtles
startx = 0
starty = 0

# Initialize direction variable
direction = 90

# Move turtles to the starting position and draw a hexagon
for t in my_turtles:
    # Set the pen up when creating the turtle object
    t.penup()

    # Move to the starting position and set the direction
    t.goto(startx, starty)
    t.setheading(direction)

    # Set the pen down after moving to the starting position
    t.pendown()

    # Draw a hexagon
    for _ in range(6):
        t.forward(50)
        t.right(60)
        t.left(30)
        t.right(20)

    # Update start position for the next turtle
    startx = t.xcor()
    starty = t.ycor()

    # Save heading for the next turtle
    direction = t.heading()

# Create a turtle screen and keep it open
wn = trtl.Screen()
wn.mainloop()
