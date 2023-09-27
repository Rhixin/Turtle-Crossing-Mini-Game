from turtle import Turtle
import turtle
import random

turtle.addshape(shape=None,name="van.gif")
turtle.addshape(shape=None,name="greencar.gif")
turtle.addshape(shape=None,name="redcar.gif")
turtle.addshape(shape=None,name="mustang.gif")
turtle.addshape(shape=None,name="bee.gif")

COLORS = ["van.gif","greencar.gif","redcar.gif","mustang.gif","bee.gif"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(COLORS))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.setheading(180)
        self.penup()
        self.goto(320,0)
        self.speed = 10
    
    def move(self):
        self.goto(self.xcor()-self.speed, self.ycor())
    
    def delete_car(self):
        self.hideturtle()