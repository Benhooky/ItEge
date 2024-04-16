from turtle import *
tracer(0)
left(90)
down()
k=30
for i in range(4):
    forward(12*k)
    right(90)
right(30)
for i in range(3):
    forward(8*k)
    right(60)
    forward(8*k)
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()
