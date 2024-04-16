from turtle import *
k =40
up()
goto(-3*k,-3*k)
down()
left(90)
dot(10)
tracer(0)
down()

for i in range(4):
    forward(14*k)
    right(90)
for i in range(5):
    forward(5*k)
    right(45)
up()
for x in range(-k*3,k*3):
    for y in range(-k*3,k*3):
        goto(x*k,y*k)
        dot(7)
done()
