from turtle import *
k=15
tracer(0)
left(90)
right(180)
forward(2*k)
right(90)
forward(40*k)
right(90)
forward(2*k)
up()
goto(0,0)

for i in range(4):
    down()
    circle(5*k,180)
    up()
    
    left(180)
up()
for x in range(-3*k,3*k):
    for y in range(-3*k,3*k):
        goto(x*k,y*k)
        dot(5)
done()