import turtle


def draw_square():
    # Turtle brad is used to draw a square on the screen
    brad = turtle.Turtle()
    brad.shape("turtle")
    # Turtle brad is shaped like a turtle. CLASSIC BRAD!
    brad.color("black", "green")
    # This makes brad greed and his line black
    brad.speed(1)
    # Brad is the slowest turtle at 1 out of 10

    # Loop to create 4 equal sides
    sq_i = 0
    while sq_i < 4:
        brad.forward(100)
        brad.right(90)
        sq_i += 1


def draw_circle():
    angie = turtle.Turtle()
    # Turtle angie is a circle because she's making a circle
    angie.shape("circle")
    angie.color("blue")
    # The circle function takes in a radius as a value and does the rest
    angie.circle(100)


def draw_triangle():
    charlie = turtle.Turtle()
    # Turtle charlie is an arrow so that he's shaped like the triangle he will create
    charlie.shape("arrow")
    charlie.color("yellow")
    # Charlie is the fastest of the three turtles, at 4 out of 10
    charlie.speed(4)
    # Charlie is told to do a 180 so he is pointing left instead of right
    charlie.left(180)

    # Loop to create 3 equal triangle sides
    tr_i = 0
    while tr_i < 3:
        charlie.forward(100)
        charlie.left(120)
        tr_i += 1


def create_window():
    # Create the window
    window = turtle.Screen()
    window.bgcolor("red")
    # Once we have a window, we can call the other functions to draw shapes
    draw_square()
    draw_circle()
    draw_triangle()
    # exitonclick needs to follow after the other commands
    window.exitonclick()


create_window()
