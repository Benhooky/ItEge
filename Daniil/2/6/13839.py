from turtle import *
tracer(0)
left(90)
k = 20
for i in range(5):
    forward(10*k)
    right(90)
    forward(16*k)
    right(90)
for i in range(6):
    left(45)
    forward(5*2**0.5*k)
    right(135)
for i in range(3):
    forward(14*k)
    left(120)
up()
for x in range(-k*4,k*4):
    for y in range(-k*4,k*4):
        goto(x*k,y*k)
        dot(4)
done()