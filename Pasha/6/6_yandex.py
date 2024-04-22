from turtle import *
tracer(0)
left(90)
k = 65
for i in range(6):
    forward(k * 7)
    right(120)
pu()
forward(k * 3)
right(90)
down()
for i in range(8):
    forward(k * 5)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(k * x, k * y)
        dot(5)
done()