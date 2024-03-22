from turtle import *
left(90)
tracer(0)
k = 15
for i in range(10):
    x,y = pos()
    goto(x+6*k,y+15*k)
    x,y = pos()
    goto(x+4*k, y-6*k)
    x,y = pos()
    goto(2*k,2*k)
    x,y = pos()
    goto((x+3*k), (y+9*k))
up()
for x in range(-k*5,k*5):
    for y in range(-k*5,k*5):
        goto(x*k,y*k)
        dot(3)
done()