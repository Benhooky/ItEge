from turtle import *
k = 30
tracer(0)
for i in range(4):
    forward(12 * k)
    right(90)
for i in range(5):
    forward(4 * k)
    right(45)
up()
for x in range(-k * 2, k * 2):
    for y in range(-k * 2, k * 2):
        goto(x * k, y * k)
        dot()
done()