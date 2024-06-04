from turtle import *
left(90)
screensize(10000, 10000)
tracer(0)
k = 30
for i in range(7):
    x,y = pos()
    goto(x+6*k,y-9*k)
    x,y = pos()
    goto(x-6*k,y+2*k)
    x,y = pos()
    goto(x+12*k,y+3*k)
up()
for x in range(-k*3,k*3):
    for y in range(-k*3,k*3):
        goto(x*k, y*k)
        dot(5)
done()