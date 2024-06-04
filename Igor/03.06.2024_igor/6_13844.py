from turtle import *
left(90)
down()
tracer(0)
k=60
screensize(10000,10000)
up()
for i in range(10):
    right(120)
    forward(12*k)
down()
for i in range(7):
    forward(7*k)
    right(90)
for i in range(5):
    right(60)
    forward(20*k)
    right(30)
up()
for x in range(-k*2,k*2):
    for y in range(-k*3,k*2):
        goto(x*k,y*k)
        dot()
done()
