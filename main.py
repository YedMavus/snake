from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snakes")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)
    snake.move()









screen.exitonclick()
