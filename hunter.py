# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    distance = 200
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, 10 * 2, 10 * 2, 20, 5)
        Pulsator.__init__(self, x, y) 
    def update(self, model):
        attack = []
        for x in set(model.simultons):
            if isinstance(x, Prey) and Mobile_Simulton.distance(self, x.get_location()) <= Hunter.distance:
                attack.append((x, Mobile_Simulton.distance(self, x.get_location())))
        if attack != []:
            prey = min(attack, key = lambda x: x[1])
            angle = (prey[0].get_location()[1] - self.get_location()[1], prey[0].get_location()[0] - self.get_location()[0])
            self.set_angle(atan2(*(angle)))
        self.move()
        return Pulsator.update(self, model)
            
        
