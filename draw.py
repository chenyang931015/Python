import turtle

def draw_square():

    brad = turtle.Turtle()

    x = 20
    n = 5
    inner = (n - 2) * 180 / n
    degree = 180 - inner

    i = 0
    while i < n:
        brad.forward(x)
        brad.right(degree)
        i = i + 1

window = turtle.Screen()

window.bgcolor("blue")

draw_square()

window.exitonclick()
