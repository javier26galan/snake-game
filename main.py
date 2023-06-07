from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initiate the objects
pepe = Snake()
food = Food()
scoreboard = Scoreboard()

# moving keys
screen.listen()
screen.onkey(pepe.up, "w")
screen.onkey(pepe.down, "s")
screen.onkey(pepe.left, "a")
screen.onkey(pepe.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    pepe.move()
    # collision with food
    if pepe.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        pepe.extend()
        scoreboard.increase_score()

    # collision with wall
    if pepe.head.xcor() > 280 or pepe.head.xcor() < -280 or pepe.head.ycor() > 280 or pepe.head.ycor() < -280:
        scoreboard.reset()
        pepe.reset()

    # collision with tail
    # pepe.segments[1:] slice the snake to don't count the head in the collision
    for segment in pepe.segments[1:]:
        if pepe.head.distance(segment) < 10:
            scoreboard.reset()
            pepe.reset()

screen.exitonclick()
