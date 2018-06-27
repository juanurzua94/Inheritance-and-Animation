# Black_Hole is derived from Simulton: i.e., it updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius * 2, Black_Hole.radius * 2 )
    def display(self, canvas):
        coordinate = self.get_location()
        canvas.create_oval(coordinate[0]-self.get_dimension()[0], coordinate[1]-self.get_dimension()[1],
                                coordinate[0]+self.get_dimension()[0], coordinate[1]+self.get_dimension()[1],
                                fill='Black')
    def update(self,model):
        eaten = set()
        for p in set(model.simultons):
            if isinstance(p, Prey) and self.contains(p):
                eaten.add(p)
                model.remove(p)
        return eaten
            
    def contains(self, prey):
        return Simulton.contains(self, prey.get_location())
