from turtle import *

colors = ["red" , "blue" , "maroon" , "yellow" , "grey"]

speed(-1)
for i in range(3,8):
    color(colors[i %len(colors)])
    for n in range(i):
        forward(100)
        left(360/i)
