from turtle import *
left(90)
tracer(0)
k=15
for i in range(4):
    forward(8*k)
    right(90)
for i in range(4):
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
        dot(5)
done()
