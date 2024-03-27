from turtle import *

left(90)
tracer(0)
down()
k = 50
up()
for i in range(10):
    right(120)
    forward(12*k)
currentX, currentY = pos()
goto(currentX-7*k, currentY+11*k)
down()
for i in range(7):
    forward(7*k)
    right(90)
for i in range(5):
    right(60)
    forward(20*k)
    right(30)
up()
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(8)
done()
