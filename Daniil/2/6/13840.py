from turtle import *
k= 30
left(90)
tracer(0)
for i in range(5):
    forward(10*k)
    right(90)
    forward(16*k)
    right(90)
for i in range(6):
    left(45)
    forward((5*2**0.5)*k)
    right(135)
for i in range(3):
    forward(14*k)
    left(120)
up()    
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
