from turtle import *
k=15
tracer(0)
left(90)
for i in range(3):
    down()
for i in range(2):
    forward(10*k)
    right(90)
    forward(10*k)
    right(90)
up()
forward(10*k)
right(90)
right(5)
left(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()
