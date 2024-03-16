from turtle import *
tracer(0)
left(90)
k = 30
for i in range(12):
    forward(4 * k)
    right(144)
    forward(4 * k)
    left(72)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()