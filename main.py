STARTING_POSITION = (0, -280)

import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
    if player.ycor() == 290:
        scoreboard.update_scoreboard()
        scoreboard.player_goal()
        player.goto(STARTING_POSITION)
        car_manager.accel()
    time.sleep(car_manager.velocity)
    screen.update()
    car_manager.create_car()
    car_manager.move()















# TODO 1: 거북이 만들기
# TODO 2: 장애물(자동차)만들기
# TODO 3: 장애물 충돌 감지하기
# TODO 4: 결승선 도달 감지하기
# TODO 5: 제임 점수판과 종료 과정 만들기