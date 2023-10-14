import turtle as t
t.left(90)
t.speed(1000)
k = 10
x = 2
t.down()
for i in range(4):
    t.forward(x * k)
    t.right(90)
    t.forward(x * k)
    t.left(90)
    t.forward(x * k)
    t.right(90)
t.up()
for i in range(0, 3 * x + 1):
    for y in range(-x, 2 * x + 1):
        t.goto(i * k, y * k)
        t.dot()
pass
