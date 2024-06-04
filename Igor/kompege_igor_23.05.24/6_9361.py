from turtle import *
dot(15)
left(90)
k=15
dot()
goto(-3*k,-4*k)
tracer(0)
right(30)
down()
for i in range(10):
    forward(14*k)
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()