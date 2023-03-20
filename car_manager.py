COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(400,400)
        self.cars = []
        self.velocity = 0.1

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(320, random.randint(-250, 280))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):
        for car in range(1, len(self.cars), 5):
            self.cars[car].forward(STARTING_MOVE_DISTANCE)

    def accel(self):
        self.velocity *= 0.9







