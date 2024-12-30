from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("snake_game\data.txt")  
        contents = file.read()  
        self.high_score = int(contents) 
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard() 


    def update_scoreboard(self):
        self.clear()    
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGMENT, font = FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard() 

    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score    
            with open("snake_game\\data.txt",'w') as data: 
                data.write(f"{self.high_score}")   
        self.score = 0 
        self.update_scoreboard()

 