from turtle import *
tracer(0)
k = 15
left(90)
for i in range(2):
    forward(5*k)
    left(90)
    back(13*k)
    left(90)
up()
back(10*k)
right(90)
forward(9*k)
left(90)
down()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(-k*3,k*3):
    for y in range(-k*3,k*3):
        goto(x*k,y*k)
        dot(4)
done()