from turtle import*
tracer(0)
left(90)
k = 25
screensize(10000, 10000)
for i in range(4):
    forward(28*k)
    right(90)
    forward(26*k)
    right(90)
up()
forward(8*k)
right(90)
forward(7*k)
left(90)
down()
for i in range(4):
    forward(67*k)
    right(90)
    forward(98*k)
    right(90)
up()
for x in range(-k*3, k*3):
    for y in range(-k*3, k*3):
        goto(x*k, y*k)
        dot(5)
done()

