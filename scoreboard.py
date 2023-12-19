from turtle import Turtle

ALIGNMENT='center'
FONT=('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        with open("highscore.txt") as data:
            self.highscore=int(data.read())
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        
        # self.write("GAME OVER!!", align=ALIGNMENT, font=FONT)
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()