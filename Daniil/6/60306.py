from turtle import *
tracer(0)
k = 20
left(90)
screensize(10000, 10000)
for i in range(4):
    forward(12*k)
    left(90)
up()
right(270)
back(-7*k)
left(180)
down()
for x in range(4):
    forward(8*k)
    right(270)
up()
for x in range(-k*3,k*3):
    for y in range(-k*3,k*3):
        goto(x*k,y*k)
        dot(5)
done()

