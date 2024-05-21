from  turtle import *
left(90)
tracer(0)
k = 25
screensize(10000, 10000)
up()
for x in range(10):
    right(120)
    forward(12*k)
down()
for x in range(7):
    forward(7*k)
    right(90)
for x in range(5):
    right(60)
    forward(20*k)
    right(30)
up()
for x in range(-k*3, k*3):
    for y in range(-k*3, k*3):
        goto(x*k, y*k)
        dot()
done()

