from turtle import *
tracer(0)
left(90)
k = 25
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
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k,y * k)
        dot(5)
done()