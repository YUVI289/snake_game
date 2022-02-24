from turtle import *
from random import randint
Up = 90
Down = 270
Right = 0
Left = 180
n = 3
xc = randint(-365,98)
yc = randint(-105,257)

list1 = []
for i in range(n):
	list1.append((xc,yc))


class Snake:
	def __init__(self):
		self.list2 = []
		self.snake_game()
		self.game_over = False

	def snake_game(self):
		n1= Turtle("turtle")
		n1.shapesize(0.7)
		n1.penup()
		n1.goto(list1[0])
		self.list2.append(n1)
		for i in range(2):
			self.add_segment(list1[i+1])
	
	def add_segment(self, i):
		snake = Turtle("square")
		snake.color("green")
		snake.shapesize(0.45)
		snake.penup()
		snake.goto(i)
		self.list2.append(snake)

	def extend(self):
		self.add_segment(self.list2[-1].pos())

	def move(self):
		for i in range(len(self.list2)-1,0,-1):
			seg = self.list2[i-1].pos()
			self.list2[i].goto(seg)
		self.list2[0].forward(11)

	def reset(self):
		for i in self.list2:
			i.goto(600,600)
		self.list2.clear()
		self.snake_game()
		self.list2[0] = self.list2[0]

	def movu(self):
		if self.list2[0].heading() != Down:
			self.list2[0].setheading(Up)
	def movd(self):
		if self.list2[0].heading() != Up:
			self.list2[0].setheading(Down)
	def movr(self):
		if self.list2[0].heading() != Left:
			self.list2[0].setheading(Right)
	def movl(self):
		if self.list2[0].heading() != Right:
			self.list2[0].setheading(Left)
	