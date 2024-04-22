from turtle import *
tracer(0)
left(90)
k = 30
back(5)
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
    back(-18)
    right(90)
up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k,y * k)
        dot(5)
done()