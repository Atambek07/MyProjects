from turtle import *
speed(0)
begin_fill()
color("black", "yellow")
for k in range(15):
    for i in range(10):
        circle(30)
        up()
        fd(20)
        down()
    up()
    goto(0, k * 10)
    down()
end_fill()
done()