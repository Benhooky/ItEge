from turtle import *
tracer(0)
k = 1
down()
left(90)
for i in range(100):
    forward(100*k)
    right(80)
up()
for x in range(-k*3, k*3):
    for y in range(-k*3, k*3):
        goto(x*k, y*k)
        dot(4)
done()