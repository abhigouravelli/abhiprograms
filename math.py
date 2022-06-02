from turtle import *
from math import *

R = 200
r = 53
a = 80
r_over_R = float(r)/R
colors = ["red","orange","yellow","green","blue","indigo","violet"]
num_colors = len(colors)

penup()
goto(0,0)

for i in range(2000):
    t = float(i)/3
    x = (R-r)*cos(r*t/R) + a * cos((1-r_over_R)*t)
    y = (R-r)*sin(r*t/R) + a * sin((1-r_over_R)*t)
    if i > 0:
        pendown()
    col = colors[i % num_colors]
    color(col)
    goto(x,y)
