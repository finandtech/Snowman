import turtle
turtle.speed(10^100)

# Snowman face

def draw_eyes(turtle, color, radius, x, y):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def draw_circle(turtle, color, x, y, radius, angle=360):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius, angle)
    turtle.end_fill()

# Main Body
draw_circle(turtle,"white",0,-120,100)
draw_circle(turtle,"white",0,30,70)
draw_circle(turtle,"white",0,150,50)



# Hat

def draw_rectangle (turtle, color, x, y, length, width):

    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pencolor("yellow")
    turtle.pensize(3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.end_fill()

draw_rectangle(turtle, "purple", -45, 230, 100, 90)
draw_rectangle(turtle, "purple", -70, 230, 140, 5)

# Stick Arms

def create_line(x, y, length, angle):
    turtle.pencolor("brown")
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)
    turtle.setheading(angle + 20)
    turtle.forward(20)
    turtle.penup()
    turtle.back(20)
    turtle.pendown()
    turtle.setheading(angle + 60)
    turtle.forward(20)
    turtle.penup()
    turtle.back(20)
    turtle.pendown()
    turtle.setheading(angle - 20)
    turtle.forward(20)
    turtle.penup()
    turtle.home()
    turtle.pencolor("brown")


# Left arm
create_line(-70, 100, 50, 160)

# Right arm
create_line(70, 100, 50, 20)

#Eyes

draw_eyes(turtle, "black", 8, 20, 200)
draw_eyes(turtle, "black", 8, -20, 200)

#Buttons

draw_eyes(turtle, "purple", 4, 0, 100)
draw_eyes(turtle, "purple", 4, 0, 80)
draw_eyes(turtle, "purple", 4, 0, 120)

#Smile

def draw_smile(turtle, color, x, y, radius, degrees):
    turtle.setheading(270)
    turtle.pencolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(radius, degrees)


draw_smile(turtle, "red", -20, 190, 20, 180)










turtle.done()









