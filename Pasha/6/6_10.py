from turtle import *
tracer(0)
color("black","red")
left(90)
k=40
begin_fill()
for i in range(2):
    forward(5*k)
    left(90)
    back(13*k)
    left(90)
end_fill()
up()
back(10*k)
right(90)
forward(9*k)
left(90)
down()
begin_fill()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
end_fill()
canvas = getcanvas()
up()
cnt = 0
for x in range(-120*k,120*k,k):
    for y in range(-120*k,120*k,k):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k,y*k)
        dot(5)
print(cnt)
done()