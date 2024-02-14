from turtle import *
tracer(0)
left(90)
k=20
for i in range(2):
    forward(3 * k)
    left(90)
    back(10 * k)
    left(90)
pu()
back(10 * k)
right(90)
forward(8 * k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
pu()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(5)
done()