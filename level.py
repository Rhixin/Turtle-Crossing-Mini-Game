from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.color("black")
        self.level = 1
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}    Highscore: {self.highscore}", font=("Courier", 12, "bold"))
    
    def game_over(self):
        if self.level > self.highscore:
            self.highscore = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.level = 1
        self.update_score()