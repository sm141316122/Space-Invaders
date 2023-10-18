from turtle import Turtle, register_shape
import random


POS = [(-135, 180), (0, 300), (135, 180)]


class Army:
    def __init__(self):
        self.army_level = 1
        self.all_army = []
        self.all_army_level_2 = []
        self.king_life = 100
        self.create_army()

    def create_army(self):
        if self.army_level == 1:
            for num in range(0, 10):
                army = Turtle()
                register_shape("img/s.gif")
                army.shape("img/s.gif")
                army.penup()
                army.goto(-360 + num*80, 100)
                self.all_army.append(army)

        elif self.army_level == 2:
            for i in range(3):
                for num in range(0, 10):
                    army = Turtle()
                    if i == 2:
                        img = "img/m.gif"
                    else:
                        img = "img/s.gif"
                    register_shape(img)
                    army.shape(img)
                    army.penup()
                    army.goto(-360 + num * 80, i*100+50)
                    if i == 2:
                        self.all_army_level_2.append(army)
                    else:
                        self.all_army.append(army)

        else:
            army = Turtle()
            register_shape("img/l.gif")
            army.shape("img/l.gif")
            army.penup()
            army.goto(0, 300)
            self.all_army.append(army)

    def hit(self, army):
        army.clear()
        army.hideturtle()
        self.all_army.remove(army)


class ArmyFire:

    def __init__(self):
        self.all_army_ammo = []

    def make_ammo(self, pos):
        ammo = Turtle("circle")
        ammo.shapesize(0.5, 0.5)
        ammo.color("white")
        ammo.penup()
        ammo.goto(pos)
        self.all_army_ammo.append(ammo)

    def make_king_ammo(self):
        pos = random.choice(POS)
        for angle in range(225, 316, 10):
            ammo = Turtle("circle")
            ammo.shapesize(0.5, 0.5)
            ammo.color("white")
            ammo.penup()
            ammo.goto(pos)
            ammo.setheading(angle)
            self.all_army_ammo.append(ammo)

    def king_shoot(self):
        for ammo in self.all_army_ammo:
            ammo.forward(2)

    def shoot(self):
        for ammo in self.all_army_ammo:
            ammo.sety(ammo.ycor() - 5)

    def hit(self, ammo):
        ammo.clear()
        ammo.hideturtle()
        self.all_army_ammo.remove(ammo)
