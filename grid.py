import random
from turtle import *
import time

max = 100
size = 25

list = []
for i in range(-max, max + size, size):
    for j in range(-max, max + size, size):
        if j + size <= max:
            set1 = {(i,j), (i, j + size)}
            list.append(set1)
        if i + size <= max:
            set2 = {(i,j), (i + size, j)}
            list.append(set2)

penup()
x = 0
y = 0
goto(x,y)
pendown()
speed(0)

start_time = time.time()
while list:
    direction = random.randint(0,4)
    original = (x,y)
    if direction == 0:
        if x < max:
            x = x + size
    elif direction == 1:
        if x > -max:
            x = x - size
    elif direction == 2:
        if y < max:
            y = y + size
    elif direction == 3:
        if y > -max:
            y = y - size
    goto(x,y)
    set1 = { original, (x,y) }
    if set1 in list:
        list.remove(set1)


end_time = time.time()
run_time = end_time - start_time
print("Run time: ", run_time)


