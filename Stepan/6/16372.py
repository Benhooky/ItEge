from turtle import *
left(90)
k = 25
screensize(10000,10000)
for i in range(2):
    forward(23*k)
    left(90)
    back(27*k)
    left(90)
up()
back(5*k)
right(90)
forward(11*k)
left(90)
down()
for i in range(2):
    forward(26*k)
    right(90)
    forward(32*k)
    right(90)
up()
for x in range(-k,k*5):
    for y in range(-k,k*2):
        goto(x*k,y*k)
        dot()
done()