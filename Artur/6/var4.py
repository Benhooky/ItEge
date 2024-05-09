from turtle import *
tracer(0)
left(90)
k = 15
up()
goto(-8*k,-8*k)
down()
for i in range(3):
    down()
    for j in range(2):
        forward(10*k)
        right(90)
        forward(10*k)
        right(90)
    up()
    forward(10*k)
    right(90)
    forward(5*k)
    left(90)
up()
for x in range(-k,k):
    for y in range(-k,k*2):
        goto(x*k, y*k)
        dot()
done()