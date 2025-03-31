from turtle import *
x = 5
k = 30
speed(5)
screensize(10000, 10000)
left(90)
forward((x+2)*k)
for i in range(4):
    forward(x*k)
    right(90)
    forward((x+2)*k)
right(90)
forward(2*x*k)
for i in range(4):
    right(90)
    forward((3*x-1)*k)
up()
for x in range(-k*2,k*2):
    for y in range(-k*2,k*2):
        goto(x*k,y*k)
        dot(5)
done()