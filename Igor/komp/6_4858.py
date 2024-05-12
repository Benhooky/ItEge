from turtle import *
dot(20)
k=40
tracer(0)
left(90)
down()
for i in range(11):
    forward(4*k)
    right(60)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()