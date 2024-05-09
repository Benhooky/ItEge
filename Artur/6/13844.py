from turtle import *
k = 50
up()
goto(10*k,10*k)
down()
up()
tracer(0)
for i in range(10):
    right(120)
    forward(12 * k)
down()
for i in range(7):
    forward(7 * k)
    right(90)
for i in range(5):
    right(60)
    forward(20 * k)
    right(30)
up()
for x in range(-k * 2, k * 2):
    for y in range(-k * 2, k * 2):
        goto(x * k, y * k)
        dot()
done()
