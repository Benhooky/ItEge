from turtle import *
tracer(0)
screensize(10000, 10000)
k = 10
left(90)
for i in range(10):
    forward(22*k)
    right(90)
    forward(16*k)
    right(90)
up()
forward(1*k)
right(90)
forward(1*k)
left(90)
down()
for i in range(10):
    forward(72*k)
    right(90)
    forward(79*k)
    right(90)
up()
for x in range(-k*3,k*15):
    for y in range(-k*3,k*15):
        goto(x*k,y*k)
        dot(4)
done()