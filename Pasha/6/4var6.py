from turtle import *
pu()
tracer(0)
left(90)
k = 15
for i in range(3):
    down()
    for j in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    pu()
    forward(10 * k)
    right(90)
    forward(5 * k)
    left(90)
for x in range(-k, k*2):
    for y in range(-k, k*3):
        goto(x * k, y * k)
        dot(5)
done()