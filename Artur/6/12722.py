from turtle import *
tracer(0)
left(90)
k = 23
for i in range(2):
    forward(5*k)
    right(45)
    forward(7*k)
    right(45)
forward(5*k)
right(90)
forward(15*k)
up()
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(4)
done()