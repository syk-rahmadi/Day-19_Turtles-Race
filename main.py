from turtle import Turtle, Screen

tum = Turtle()
screen = Screen()


def move_forwards():
    tum.forward(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.exitonclick()

