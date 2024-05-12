from turtle import *
k=20
tracer(0)
left(90)
down()
for i in range(95):
    forward(5*k)
    right(72)
    back(5*k)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()