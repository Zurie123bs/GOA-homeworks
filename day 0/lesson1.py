from turtle import *

#we wantto paint a house

#step 1:  draw a square
shape("square")
speed(10)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# left window
penup()
goto(0,90)
pendown()
color("black")     
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


#right window
penup()
goto(200,90)
pendown()
begin_fill()
left(270)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#end of house





exitonclick()