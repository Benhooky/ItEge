from turtle import *
left(90)
tracer(0)
up()
k = 11
for i in range(10):
    right(120)
    forward(10*k)
down()
for i in range(7):
    forward(15*k)
    right(90)
for i in range(5):
    right(60)
    forward(20*k)
    right(30)
up()
for x in range(-k*4,k*4):
    for y in range(-k*4,k*4):
        goto(x*k,y*k)
        dot(4)
done()