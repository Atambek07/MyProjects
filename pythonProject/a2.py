from turtle import *
shape('turtle')
width(5)
speed(15)

begin_fill()
color("red")
for i in range(4):
    fd(100)
    lt(90)
end_fill()
rt(90)
begin_fill()
color("blue")
for i in range(4):
    fd(100)
    lt(90)
end_fill()
begin_fill()
rt(90)
color("green")
for i in range(4):
    fd(100)
    lt(90)
end_fill()
begin_fill()
rt(90)
color("yellow")
for i in range(4):
    fd(100)
    lt(90)
end_fill()
done()
