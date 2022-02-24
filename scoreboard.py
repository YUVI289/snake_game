from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(250,230)
        self.scoreupd()
        self.hideturtle()
        self.penup()
    
    def scoreupd(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align = "center", font = ("Arial", 25, "normal"))

    def higsco(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.scoreupd()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align = "center", font = ("Arial",25, "normal"))
        
    
    def incsc(self):
        self.score+=1
        self.scoreupd()