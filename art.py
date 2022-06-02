from turtle import *

colors = ["red","orange","blue","green","black","grey"]
num_colors = len(colors)

speed(0)
hideturtle()
penup()
angle = 0

for size in range(1,400):
    goto(0,0)
    setheading(angle)
    forward(size)
    dot(10 + size/30, colors[size%num_colors])
    angle = angle + 50
