import turtle


def draw_square(a_turtle):
    for i in range(0, 4):
        a_turtle.forward(100)
        a_turtle.right(90)


def draw_circle(a_turtle):
    a_turtle.circle(100)


def draw_triangle(a_turtle):
    for i in range(0, 3):
        a_turtle.forward(100)
        a_turtle.left(120)


def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black", "green")
    brad.speed(10)
    # angie = turtle.Turtle()
    # angie.shape("circle")
    # angie.color("blue")
    # charlie = turtle.Turtle()
    # charlie.shape("arrow")
    # charlie.color("yellow")
    # charlie.speed(4)
    # charlie.left(180)
    for i in range(0, 72):
        draw_square(brad)
        brad.right(95)
    # draw_square(brad)
    # draw_circle(angie)
    # draw_triangle(charlie)
    window.exitonclick()


draw_turtles()
