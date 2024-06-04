from turtle import *
tracer(0)
k=15
for i in range(13):
    x,y=pos()
    goto(x+6*k,y+3*k)
    x,y=pos()
    goto(x-6*k,y+2*k)
    x,y=pos()
    goto(x-4*k,y-1*k)
    x,y=pos()
    goto(x+4*k,y-4*k)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot()
done()