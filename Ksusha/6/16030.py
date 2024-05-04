from turtle import *
k=50
up()
goto(0,7*k)
down()
tracer(0)
left(90)
right(135)
for x in range(4):
    forward(10*k)
    right(90)
right(45)
up()
forward(9.5*k)
down()
right(90)
for x in range(360):
    forward(0.1*k)
    right(1)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(6)
done()