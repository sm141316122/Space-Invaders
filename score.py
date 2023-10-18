from turtle import Turtle
import time


POS = [(-680, 390), (-450, 390), (0, 0)]


class Score:

    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.all_score = []
        self.create_score_ui(POS)
        self.show_score()

    def create_score_ui(self, position):
        for pos in position:
            score_ui = Turtle()
            score_ui.color("white")
            score_ui.hideturtle()
            score_ui.penup()
            score_ui.goto(pos)
            self.all_score.append(score_ui)

    def show_score(self):
        self.all_score[0].write(f"Hi-Score: {self.high_score}", font=("Arial", 24, "bold"))
        self.all_score[1].write(f"Score: {self.score}", font=("Arial", 24, "bold"))

    def refresh_score(self):
        self.score += 1
        self.all_score[1].clear()
        self.all_score[1].write(f"Score: {self.score}", font=("Arial", 24, "bold"))

    def complete(self, on):
        if on:
            text = "Complete"
        else:
            text = "Game Over"
        ui = self.all_score[2]
        ui.write(f"{text}", font=("Arial", 48, "bold"), align="center")
        time.sleep(3)
        if on:
            ui.clear()
