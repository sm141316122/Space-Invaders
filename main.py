from turtle import Screen
from ship import Ship, Fire, Life
from army import Army, ArmyFire
from score import Score
import time
import random


screen = Screen()
screen.title("Space Invaders")
screen.setup(width=1500, height=900)
screen.bgcolor("black")
screen.tracer(0)

ship = Ship()
fire = Fire()
life = Life()

army = Army()
army_fire = ArmyFire()

score = Score()

screen.listen()
screen.onkeypress(ship.move_left, "Left")
screen.onkeypress(ship.move_right,  "Right")

game_on = True
army_fire_cd = 0
fire_cd = 0
while game_on:
    time.sleep(0.005)

    if fire_cd == 0 or fire_cd % 40 == 0:
        if len(army.all_army) != 0 or len(army.all_army_level_2) != 0:
            fire.make_ammo(ship.xcor())

        if len(fire.all_ammo) == 0 and len(army_fire.all_army_ammo) == 0:
            ship.reset_ship()
            army.army_level += 1
            score.complete(game_on)
            if army.army_level > 3:
                break
            else:
                army.create_army()

    fire_cd += 1
    army_fire_cd += 1

    fire.shoot()

    if fire_cd == 80:
        if army.army_level == 2:
            if len(army.all_army_level_2) != 0:
                choice = random.choice(army.all_army_level_2)
                army_fire.make_ammo((choice.xcor(), choice.ycor()))
        fire_cd = 0

    if army_fire_cd == 240:
        if army.army_level == 3:
            if len(army.all_army) != 0:
                army_fire.make_king_ammo()
        army_fire_cd = 0

    if army.army_level > 1:
        if army.army_level == 2:
            army_fire.shoot()
            for ammo in fire.all_ammo:
                for a in army.all_army_level_2:
                    if ammo.distance(a) < 40:
                        fire.hit(ammo)
                        a.clear()
                        a.hideturtle()
                        army.all_army_level_2.remove(a)
                        score.refresh_score()
        else:
            army_fire.king_shoot()

        for ammo in army_fire.all_army_ammo:
            if ammo.distance(ship) < 25:
                life.get_hit()
                army_fire.hit(ammo)

            if ammo.ycor() < -410:
                army_fire.hit(ammo)

    for ammo in fire.all_ammo:
        for a in army.all_army:
            if army.army_level == 3:
                if -250 < ammo.xcor() < 250:
                    if ammo.ycor() > 200:
                        fire.hit(ammo)
                        army.king_life -= 1
                        score.refresh_score()
                        if army.king_life == 0:
                            army.hit(a)
            else:
                if ammo.distance(a) < 40:
                    fire.hit(ammo)
                    army.hit(a)
                    score.refresh_score()

        if ammo.ycor() > 410:
            fire.hit(ammo)

    if len(life.life) == 0:
        game_on = False

    screen.update()

if not game_on:
    score.complete(game_on)

screen.exitonclick()
