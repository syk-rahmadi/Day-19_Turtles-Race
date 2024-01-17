from turtle import Turtle, Screen

tem = Turtle()
tem.shape("turtle")
tem.color("green")
tem.speed("fastest")
tem.pensize(3)
screen = Screen()


def move_forwards():
    tem.forward(10)

def move_backwards():
    tem.backward(10)

def turn_left():
    tem.left(10)

def turn_right():
    tem.right(10)

def clear():
    tem.clear()
    tem.penup()
    tem.home()
    tem.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()

