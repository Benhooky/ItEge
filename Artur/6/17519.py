from turtle import *
tracer(0)
k = 15
left(90)
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
up()

for x in range(-k * 5, k * 5):
    for y in range(-k * 5, k * 5):
        goto(x * k, y * k)
        dot(4)

done()