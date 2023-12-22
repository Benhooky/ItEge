from turtle import *
tracer(0)
left(90)
k=40
for i in range(7):
    forward(10*k)
    right(120)
pu()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(5)
done()