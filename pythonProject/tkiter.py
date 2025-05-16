from turtle import *
fillcolor('red')
begin_fill()
speed(9999999)
left(140)
forward(224)
for _ in range(200):
    right(1)
    forward(2)
left(120)
for _ in range(200):
    right(1)
    forward(2)
forward(224)
end_fill()

up()
goto(-300,300)
down()

done()