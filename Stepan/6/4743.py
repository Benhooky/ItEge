from turtle import *
screensize(10000, 10000)
tracer(0)
k = 6
left(90)
for i in range(10):
    forward(15*k)
    right(60)

up()
for x in range(-k*15,k*15):
    for y in range(-k*15,k*15):
        goto(x*k, y*k)
        dot(4)
done()
