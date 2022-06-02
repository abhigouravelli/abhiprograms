import turtle
import random

def draw_slice(x,y,radius,start_angle,slice_angle,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(start_angle)
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, slice_angle)
    turtle.goto(x, y)
    turtle.penup()
    turtle.end_fill()

draw_slice(0, 0, 100, 0, 30, "red")

turtle.setheading(0)
turtle.speed(0)
colors = ["red","green","orange","indigo","violet","black"]
num_colors = len(colors)
data = [43, 97, 119, 21, 36, 59, 102, 75, 90, 65]
total_data = sum(data)
num_data = len(data)
min_slice_size = 30
max_slice_size = 70
total_angle = 0
index = 0

while total_angle < 360:
    slice_angle = random.randint(min_slice_size, max_slice_size)
    if(slice_angle + total_angle > 360):
        slice_angle = 360 - total_angle
    index %= num_colors
    draw_slice(0,0,100,total_angle,slice_angle,colors[index])
    total_angle += slice_angle
    index += 1

for i in range(10):
    slice_angle = float(data[i])/total_data * 360
    x = random.randint(-150, 150)
    y = random.randint(-150,150)
    radius = random.randint(50,150)
    index = 0
    total_angle = 0

    while total_angle < 360:
        slice_angle = random.randint(min_slice_size, max_slice_size)
        if (slice_angle + total_angle > 360):
            slice_angle = 360 - total_angle
        index %= num_colors
        draw_slice(x,y,radius,total_angle,slice_angle,colors[index])
        total_angle += slice_angle
        if index > 9:
            break
        else:
            index += 1
        




