from turtle import *
left(90)
tracer(0)
down()
k = 25
for i in range(2):
    forward(5*k)
    right(45)
    forward(7*k)
    right(45)
forward(5*k)
right(90)
forward(15*k)
up()
for x in range(-k*4,k*4):
    for y in range(-k*4,k*4):
        goto(x*k,y*k)
        dot(5)
done()
