#Olümpiarõngad Nikita
import turtle
## Aken

win = turtle.Screen()
win.setup(width=500, height=400)
win.title("Nikita - Olümpiarõngad")
#Liigtutan õigesse kohta
turtle.speed(0)
turtle.up()
turtle.goto(-150,50)
turtle.down()

##Ring 1
turtle.pensize(6)
turtle.pencolor("blue")
turtle.circle(50)

turtle.up()
turtle.goto(-40,50)
turtle.down()

##Ring 2
turtle.pensize(6)
turtle.pencolor("black")
turtle.circle(50)

##Ring 3
turtle.up()
turtle.goto(70,50)
turtle.down()

turtle.pensize(6)
turtle.pencolor("red")
turtle.circle(50)

##Ring 4
turtle.up()
turtle.goto(15,-5)
turtle.down()

turtle.pensize(6)
turtle.pencolor("green")
turtle.circle(50)

##Ring 5

turtle.up()
turtle.goto(-100,-5)
turtle.down()

turtle.pensize(6)
turtle.pencolor("yellow")
turtle.circle(50)

turtle.done()