from turtle import *
tracer(0)
left(90)
k=30
for i in range(4):
    forward(12*k)
    right(90)
for i in range(5):
    forward(4*k)
    right(45)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()