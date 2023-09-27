from turtle import Turtle, Screen
import turtle
from character import Character
from level import Level
import time
from car import Car
import random
import winsound



#screen options
sc = Screen()
sc.bgpic("bg.png")
sc.setup(600,600)
sc.tracer(0)
sc.title("Crossing Game")

#player options
player = Character()

#level display options
level = Level()

#even listeners
turtle.listen()
turtle.onkeypress(key="space", fun=player.move)
turtle.onkeyrelease(key="space", fun=player.change_shape)

#car options 
cars = []
car = Car()
cars.append(car)
x = 12
speeds_list = [8,10,12]
y_cor = []
for i in range(-160,190,30):
    y_cor.append(i)      
    
    
#functions   
def get_speed():
    global speeds_list
    return random.choice(speeds_list)

game_on = True

while game_on:
    sc.update()
    time.sleep(0.1)
    
    #gnerate new car after car went to screen
    if car.xcor() < 290:
        car = Car()
        car.speed = get_speed()
        car.goto(car.xcor(), random.choice(y_cor))
        cars.append(car)
    
    #move all the cars 
    for i in cars:
        #remove car after to avoid too much memory
        if i.xcor() < -310:
            cars.remove(i)
            i.delete_car()
            
        i.move()
    
    #check game_over
    for i in cars:
        if i.distance(player) < 20:
            sc.update()
            winsound.PlaySound("splat.wav", winsound.SND_PURGE)
            level.game_over()
            player.reset() 
    
    #player win level
    if player.ycor() > 260:
        winsound.PlaySound("nextlevel.wav",winsound.SND_PURGE)
        level.level +=1
        level.update_score()
        player.reset()
        x+=4
        speeds_list.append(x)
    
    

sc.exitonclick()
