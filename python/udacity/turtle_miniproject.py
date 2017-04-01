import turtle


def draw_diamond(a_turtle):
    for i in range(0, 2):
        a_turtle.forward(50)
        a_turtle.right(45)
        a_turtle.forward(50)
        a_turtle.right(135)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    amanda = turtle.Turtle()
    amanda.shape("turtle")
    amanda.color("yellow", "red")
    amanda.speed(10)
    amanda.setheading(270)
    for i in range(0, 36):
        draw_diamond(amanda)
        amanda.right(10)
    amanda.forward(500)
    amanda.right(90)
    amanda.forward(500)
    amanda.right(180)
    amanda.forward(1000)
    amanda.penup()
    amanda.left(90)
    amanda.forward(250)
    amanda.left(90)
    amanda.forward(250)
    amanda.left(45)
    amanda.pendown()
    amanda.forward(100)
    amanda.left(90)
    amanda.forward(100)
    amanda.penup()
    amanda.left(45)
    amanda.forward(50)
    amanda.pendown()
    amanda.left(90)
    amanda.forward(142)
    amanda.right(135)
    amanda.forward(100)
    amanda.right(90)
    amanda.forward(100)
    amanda.right(135)
    amanda.penup()
    amanda.forward(72)
    amanda.right(90)
    amanda.forward(30)
    window.exitonclick()


draw_art()
