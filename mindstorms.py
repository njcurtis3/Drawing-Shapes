import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("dark green")
    brad.pen(fillcolor="black", pencolor="green", pensize=10)
    brad.shapesize(outline=1)
    brad.speed(2)
    for i in range(1, 36):
        draw_square(brad)
        brad.forward(500)
        brad.right(10)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.pen(pensize=6)
    angie.circle(300)

def draw_triangle():
    sam = turtle.Turtle()
    sam.shape("turtle")
    sam.color("purple")
    sam.speed(2)
    sam.shapesize(outline=1)
    sam.pen(pensize=6)
    for i in range(0, 3):
        sam.forward(500)
        sam.left(120)

draw_shapes()
