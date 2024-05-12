from turtle import *
k = 10
tracer(0)
left(90)
dot(10)
for i in range(15):
    for j in range(20):
        forward(40*k)
        right(90)
    left(90)
up()
for x in range(-k*6,k*6):
    for y in range(-k*6,k*6):
        goto(x*k,y*k)
        dot(4)
done()