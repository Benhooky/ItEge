from turtle import *
left(90)
tracer(0)
down()
k =25
for i in range(2):
    forward(3*k)
    left(90)
    back(10*k)
    left(90)
up()
back(10*k)
right(90)
forward(8*k)
left(90)
down()
for i in range(2):
    forward(16*k)
    right(90)
    forward(8*k)
    right(90)
up()
for x in range(-k*4,k*4):
    for y in range(-k*4,k*4):
        goto(x*k,y*k)
        dot(5)
done()
