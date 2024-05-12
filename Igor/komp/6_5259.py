from turtle import *
k=20
up()
dot(k)
goto(10*k,15*k)
tracer(0)
left(90)
down()
for i in range(15):
    for i1 in range(20):
        forward(40*k)
        right(90)
    left(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()