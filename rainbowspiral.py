import random

def getAverage(color1, color2):
    r = (color1[0] + color2[0])/2
    g = (color1[1] + color2[1])/2
    b = (color1[2] + color2[2])/2

def getGradient(color_list):
    result = []
    for i in range(len(color_list)):
        if i+1 == len(color_list):
            result.append(color_list[i])
            average = getAverage(color_list[i], color_list[0])
            result.append(average)
        else:
            result.append(color_list[i])
            average = getAverage(colors[i], colors[i + 1])
            result.append(average)
    return result

red = [225,0,0]
orange = [225, 128, 0]
yellow = [255, 255, 0]
green = [0,255,0]
blue = [0,0,255]
purple = [128,0,225]

colors = [red, orange, yellow, green, blue, purple]
gradientColors = getGradient(colors) 
betterGradientColors = getGradient(gradientColors) 
bestGradientColors = getGradient(betterGradientColors) 
turtle.speed(0)

for x in range(720):
    index = int(x/20) % len(bestGradientColors)
    color = bestGradientColors[index]
    turtle.pencolor(color)
    turtle.forward(x)
    turtle.left(121)
