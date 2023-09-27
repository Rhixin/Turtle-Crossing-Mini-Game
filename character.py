from turtle import Turtle,addshape
import winsound

addshape(shape=None,name="turt.gif")
addshape(shape=None,name="turtwalk.gif")


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.reset()
        
    def move(self):
        winsound.PlaySound("jump.wav",winsound.SND_ASYNC)
        self.forward(20)
        self.shape("turtwalk.gif")
        
    def reset(self):
        self.shape("turt.gif")
        self.goto(0,-260)
        self.setheading(90)
    
    def change_shape(self):
        self.shape("turt.gif")
        

        
    
    