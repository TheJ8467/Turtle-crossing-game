FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def player_goal(self):
        self.level += 1
        self.update_scoreboard()
