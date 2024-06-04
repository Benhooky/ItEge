from turtle import *
left(90)
k=15
dot()
tracer(0)
screensize(10000,10000)
down()
for i in range(4):
    forward(10*k)
    right(270)
up()
forward(3*k)
right(270)
forward(5*k)
right(90)
down()
for i in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)
up()
for x in range(-k*2,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()