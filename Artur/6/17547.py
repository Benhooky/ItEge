k = 10
from turtle import *
screensize(10000, 10000)
tracer(0)
left(90)
for i in range(3):
    forward(7 * k)
    right(90)
    forward(12 * k)
    right(90)
up()
forward(4 * k)
right(90)
forward(6 * k)
left(90)
down()
for i in range(4):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)
up()
for x in range(-k * 10, k * 10): 
    for y in range(-k * 10, k * 10):
        goto(x * k, y * k)
        dot(4)
done()