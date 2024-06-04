from turtle import *
screensize(10000, 10000)
tracer(0)
k = 6
left(90)
right(45)
for i in range(25):
    forward(55*k)
    right(90)

up()
for x in range(-k*15,k*15):
    for y in range(-k*15,k*15):
        goto(x*k, y*k)
        dot(3)
done()
