import turtle as trtl

# Setting up an empty list for turtlesi
my_turtles = []

# Defining interesting shapes and colors for turtles
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Creating turtles with specified shapes and adding them to the list
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)

# Starting position for turtles
startx = 0
starty = 0

# Moving turtles to the starting position and drawing
for t in my_turtles:
    t.goto(startx, starty)
    t.right(45)
    t.forward(50)

    # Updating start position for the next turtle
    startx = startx + 50
    starty = starty + 50

# Creating a turtle screen and keeping it open
wn = trtl.Screen()
wn.mainloop()


# Moving turtles to the starting position and setting the pen up
for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(45)
    t.forward(50)

    # Updating start position for the next turtle
    startx = startx + 50
    starty = starty + 50

# Moving turtles to the starting position and drawing where the last turtle left off
prev_x, prev_y = startx, starty
for t in my_turtles:
    t.penup()
    t.goto(prev_x, prev_y)
    t.pendown()
    t.right(45)
    t.forward(50)

    # Updating previous position for the next turtle
    prev_x, prev_y = t.xcor(), t.ycor()
