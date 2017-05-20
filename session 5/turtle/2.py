from turtle import *

def draw_square(i, cl):
    color(cl)
    for _ in range(4):
        fd(i)
        left(90)
        
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
