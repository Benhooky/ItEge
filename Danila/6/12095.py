from turtle import *
left(90)
tracer(0)
k = 80
for i in range(12):
    forward(4*k)
    right(144)
    forward(4*k)
    left(72)
up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot(5)
done()