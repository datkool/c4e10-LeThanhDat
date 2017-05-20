from turtle import *

def draw_star(x,y,length):
    pu()
    goto(x,y)
    pd()
    for _ in range(5):
        fd(length)
        rt(144)

draw_star(0,50,50)
