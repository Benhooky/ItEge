from turtle import *
left(90)
tracer(0)
k = 30
up()
goto(-10*k,-10*k)
down()
for i in range(2):
    forward(13*k)
    right(90)
    forward(18*k)
    right(90)
up()
forward(5*k)
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
        goto(x*k, y*k)
        dot()
done()