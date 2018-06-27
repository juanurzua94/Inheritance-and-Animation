# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
from random import uniform


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius * 2, Floater.radius * 2, random(), 5 )
    def update(self, model):
        self.move()
        if random() <= .3:
            speed_adjust = uniform(-.5, .5)
            if self.get_speed() + speed_adjust <= 7 and self.get_speed() >= 3:
                self.set_speed(self.get_speed() + speed_adjust)
            angle_adjust = uniform(-.5, .5)
            self.set_angle(self.get_angle() + angle_adjust)
    def display(self, canvas):
        coordinate = self.get_location()
        canvas.create_oval(coordinate[0]-Floater.radius, coordinate[1]-Floater.radius,
                                coordinate[0]+Floater.radius, coordinate[1]+Floater.radius,
                                fill='red')
