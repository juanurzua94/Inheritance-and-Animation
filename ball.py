# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

import math, random
from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self,x,y, Ball.radius * 2, Ball.radius * 2,  math.pi * 2, 5)
    def update(self, model):
        self.move()
    def display(self, canvas):
        coordinate = self.get_location()
        canvas.create_oval(coordinate[0]-Ball.radius, coordinate[1]-Ball.radius,
                                coordinate[0]+Ball.radius, coordinate[1]+Ball.radius,
                                fill='blue')
    
