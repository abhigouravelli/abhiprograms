import turtle
def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y-size)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

tom = turtle.Turtle()
tom.speed(0)
tom.hideturtle()
colors = ["red", "black", "green", "blue", "green", "violet", "orange"]
num_colors = len(colors)

for i in range(50):
    size = 3 * i
    color = colors[i % num_colors]
    diameter = 2 * i
    draw_circle(tom, color, diameter, size, size)
    draw_circle(tom, color, diameter, -size, size)
    draw_circle(tom, color, diameter, -size, -size)
    draw_circle(tom, color, diameter, size, -size)

