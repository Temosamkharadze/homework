from tkinter import RIGHT
from turtle import *

#we want to print a house

width(7)
speed(30)

shape("turtle")

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)



forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()




penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
penup()
forward(100)
left(90)
forward(25)
pendown()

begin_fill()
color("brown")

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)

end_fill()

penup()
forward(150)
pendown()
right(90)
begin_fill()

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)
end_fill()










exitonclick()