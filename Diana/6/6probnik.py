from turtle import *
tracer(0)
dot(10)
left(90)
k = 20
back(5*k)
for i in range(2):
    forward(12*k)
    right(90)
    forward(16*k)
    right(90)
up()
forward(3*k)
right(90)
forward(5*k)
left(90)
down()
for i in range(2):
    forward(12*k)
    left(270)
    back(-18*k)
    right(90)
up()
for x in range(-k,k*2):
    for y in range(-k,k):
        goto(x*k, y*k)
        dot(5)
done()