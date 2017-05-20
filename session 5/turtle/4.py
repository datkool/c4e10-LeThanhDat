from turtle import *

def draw_star(x,y,length):
    pu()
    goto(x,y)
    pd()
    for _ in range(5):
        fd(length)
        rt(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)



#random.randint select random value from 3 to 10
