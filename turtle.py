from turtle import *
from random import randint

class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.points = 0
    
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        return distance < 30

tsize = 20
s_width = 200
s_height = 180
 
player = Sprite(0, -100, 10, 'circle', 'orange')
enemy1 = Sprite(-s_width, 0, 15, 'square', 'red')
enemy2 = Sprite(s_width, 70, 15, 'square', 'red')
goal = Sprite(0, 120, 20, 'triangle', 'green')
 
scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

total_score = 0
while total_score < 3:
    if player.is_collide(goal):
        player.goto(0, -100)
    total_score += 1
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        break
enemy1.hideturtle()
enemy2.hideturtle()

