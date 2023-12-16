from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")


game_is_on = True
    
while game_is_on:
    screen.update()
    if scoreboard.score<10:
        time.sleep(0.1)
    elif scoreboard.score<20:
        time.sleep(0.07)
    else:
        time.sleep(0.04)

    snake.move()

    # Detect colission with food
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
    

    #Detect collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # game_is_on = False
        # scoreboard.reset()
    if snake.head.xcor() > 280:
        snake.head.goto(-280,snake.head.ycor())
    elif snake.head.xcor() < -280:
        snake.head.goto(280,snake.head.ycor())
    elif snake.head.ycor() > 280:
        snake.head.goto(snake.head.xcor(),-280)
    elif snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(),280)
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on=False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()