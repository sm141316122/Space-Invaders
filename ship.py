from turtle import Turtle, register_shape


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        register_shape("img/ship.gif")
        self.shape("img/ship.gif")
        self.penup()
        self.goto(0, -350)

    def move_left(self):
        self.setx(self.xcor() - 15)

    def move_right(self):
        self.setx(self.xcor() + 15)

    def reset_ship(self):
        self.goto(0, -350)


class Fire:

    def __init__(self):
        self.all_ammo = []

    def make_ammo(self, pos):
        ammo = Turtle("square")
        ammo.shapesize(1, 0.3)
        ammo.color("red")
        ammo.penup()
        ammo.goto(pos, -325)
        self.all_ammo.append(ammo)

    def shoot(self):
        for ammo in self.all_ammo:
            ammo.sety(ammo.ycor() + 5)

    def hit(self, ammo):
        ammo.clear()
        ammo.hideturtle()
        self.all_ammo.remove(ammo)


class Life:

    def __init__(self):
        self.life = []
        self.reset_life()

    def reset_life(self):
        self.life = []
        for num in range(10):
            life = Turtle("square")
            life.shapesize(1, 6)
            life.color("white")
            life.penup()
            life.goto(-540 + num*120, -420)
            self.life.append(life)

    def get_hit(self):
        self.life[-1].clear()
        self.life[-1].hideturtle()
        self.life = self.life[:-1]
