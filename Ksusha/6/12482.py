from turtle import *
k=30
tracer(0)
left(90)
down()
for x in range(4):
    forward(8*k)
    right(90)
for x in range(4):
    left(30)
    forward(6*k)
    right(30)
    forward(8*k)
    right(150)
    forward(6*k)
    left(60)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()