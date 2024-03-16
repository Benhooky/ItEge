from turtle import *
left(90)
tracer(0)
up()
k = 25
for i in range(10):
    right(120)
    forward(12*k)
down()
for i in range(7):
    forward(7*k)
    right(90)
for i in range(5):
    right(60)
    forward(20*k)
    right(30)
up()
for x in range(-k*4,k*4):
    for y in range(-k*4,k*4):
        goto(x*k,y*k)
        dot(2)
done()