from turtle import *
shape('turtle')

begin_fill()
color("green")
goto(-200,0)
goto(-50,-50)
goto(0,0)
end_fill()

goto(-200,0)
goto(-50,50)
goto(0,0)

begin_fill()
color("green")
goto(200,0)
goto(50,50)
goto(0,0)
end_fill()

goto(200,0)
goto(50,-50)
goto(0,0)


begin_fill()
color("red")
goto(0,200)
goto(-50,50)
goto(0,0)
end_fill()

goto(0,200)
goto(50,50)
goto(0,0)

begin_fill()
color("red")
goto(0,-200)
goto(50,-50)
goto(0,0)
end_fill()

goto(0,-200)
goto(-50,-50)
goto(0,0)
done()