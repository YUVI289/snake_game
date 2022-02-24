from turtle import *
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

score = 0

title("Snake")
screen = Screen()
bor1 = Turtle()
screen.tracer(0)	
screen.setup(900,600)
screen.bgpic("bg.png")
screen.addshape("bord.gif")
bor1.shape("bord.gif")
bor1.penup()
bor1.setposition(-140,75)
lev = screen.numinput("Level","Press easy-1, medium-2, hard-3.")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.movu, "Up")
screen.onkey(snake.movd, "Down")
screen.onkey(snake.movr, "Right")
screen.onkey(snake.movl, "Left")
	
game_over = False
while not game_over:
	screen.update()
	time.sleep(0.1/lev)
	snake.move()
	if snake.list2[0].distance(food)<9:
		food.reassign()
		snake.extend()
		scoreboard.incsc()

	if snake.list2[0].xcor() > 98 or snake.list2[0].xcor() < -380 or snake.list2[0].ycor() < -105 or snake.list2[0].ycor() > 257:
		scoreboard.higsco()
		snake.reset()

	for i in snake.list2[1:]:
		if snake.list2[0].distance(i)<10:
			scoreboard.higsco()
			snake.reset()

screen.exitonclick()