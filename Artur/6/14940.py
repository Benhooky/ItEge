from turtle import *
k = 15
tracer(0)
for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(14 * k)
left(90)
down()
for i in range(2):
    forward(17 * k)
    right(90)
    forward(7 * k)
    right(90)
up()
for x in range(-k * 2, k * 2):
    for y in range(-k * 2, k * 2):
        goto(x * k, y * k)
        dot()
done()
