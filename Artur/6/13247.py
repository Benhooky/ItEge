from turtle import *
k = 40
screensize(10000, 10000)
tracer(0)
up()
goto(-28*k,32*k)
down()
tracer(0)
for i in range(243):
    forward(78 * k)
    right(120)
up()
for x in range(-k * 4, k *4):
    for y in range(-k * 4, k * 4):
        goto(x * k, y * k)
        dot()
done()
