from turtle import *
tracer(0)
left(90)
k = 35
for i in range(4):
    forward(13*k)
    right(120)
up()
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(4)
done()