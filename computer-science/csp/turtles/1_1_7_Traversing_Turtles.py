import turtle

my_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = turtle.Turtle(shape=s)
    my_turtles.append(t)

startx = 0
starty = 0
direction = 90

for t in my_turtles:
    t.color(turtle_colors.pop())
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(-direction + 45)
    t.forward(50)

    direction = t.heading()
    startx = t.xcor()
    starty = t.ycor()

wn = turtle.Screen()
wn.mainloop()
