from turtle import *
tracer(0)
left(90)
k = 18
for i in range(3):
    down()
    for i in range(2):
        forward(7*k)
        right(90)
        forward(7*k)
        right(90)
    up()
    forward(6*k)
    right(90)
    forward(6*k)
    left(90)
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(4)
done()