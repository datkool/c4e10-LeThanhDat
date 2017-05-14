from turtle import *

speed(-1)

colors = ["red" , "blue" , "maroon" , "yellow" , "grey"]

for i in range(5):
    color(colors[i])
    begin_fill()
    for n in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
