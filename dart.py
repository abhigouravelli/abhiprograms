from turtle import *
from random import randint


total_score = 0
size = 150
speed(0)

colors = ["red","black"]
index = 0
for radius in range(size,0,-25):
    dot(radius, colors[index])
    index = 1 - index


for angle in range(0, 360, 30):
    penup()
    goto(0,0)
    setheading(angle)
    pendown()
    forward(size)


for i in range(10):
    input("Press ENTER to shoot")
    distance = randint(0, size)
    angle = randint(0, 360)
    goto(0,0)
    setheading(angle)
    forward(distance)
    dot(5,"yellow")
    hit_score = size - radius
    print(hit_score)
    total_score = total_score + hit_score

print("Your total score is: ", total_score)
scores = ["Awfull","Poor","Fair","Adequate","OK","Good","Great","Excellent","Outstanding","Phenomal"]
print(scores[int(total_score/size)])


