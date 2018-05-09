import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(this_turtle):
    this_turtle.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("dark green")
    angie.speed(500)

    Tom = turtle.Turtle()
    Tom.shape("circle")
    Tom.color("dark green")
    Tom.speed(500)

    for i in range(1,37):
        draw_square(Tom)
        Tom.right(10)

    for i in range(37,38):
        Tom.right(90)
        Tom.forward(300)

    for i in range(38,76):
        draw_square(Tom)
        Tom.right(10)

    for i in range(76,77):
        Tom.right(70)
        Tom.forward(300)

    for i in range(77,115):
        draw_square(Tom)
        Tom.right(10)

    for i in range(115,116):
        Tom.right(70)
        Tom.forward(300)

        window.exitonclick()

draw_art()
