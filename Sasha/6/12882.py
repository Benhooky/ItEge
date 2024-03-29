from turtle import *
left(90)
tracer(0)
down()
k = 35
left(255)
for i in range(3):
    left(30)
    for i in range(4):
        forward(10*k)
        left(90)
up()
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(4)
done()
