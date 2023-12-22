from turtle import *
color("black","red")
speed(1000)
m = 100
begin_fill()
left(90)
right(30)
for i in range(4):
    forward(25*m)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-120*m,120*m,m):
    for y in range(-120*m,120*m,m):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
print(cnt)
done()
exit()