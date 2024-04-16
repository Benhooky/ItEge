from turtle import *
left(90)
dot(10)
tracer(0)
down()
k = 25
for i in range(6):
    right(36)
    forward(10*k)
    right(36)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(3)
done()
