from mobilesimulton import Mobile_Simulton
from hunter import Hunter
from math import atan2
#This Special class searches and kills the hunter
#"The hunter is hunted"
class Special(Mobile_Simulton):
    radius = 8
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, Special.radius * 2, Special.radius * 2, 20, 8)
        
    def update(self, model):
        attack = []
        for x in set(model.simultons):
            if isinstance(x, Hunter) and Mobile_Simulton.distance(self, x.get_location()) <= 100:
                attack.append((x, Mobile_Simulton.distance(self, x.get_location())))
        if attack != []:
            hunt_the_hunter = min(attack, key = lambda x: x[1])
            angle = (hunt_the_hunter[0].get_location()[1] - self.get_location()[1], hunt_the_hunter[0].get_location()[0] - self.get_location()[0])
            self.set_angle(atan2(*(angle)))
        self.move()
        return self.kill(model)
    
    def kill(self, model):
        killed = set()
        for x in set(model.simultons):
            if isinstance(x, Hunter) and self.contains(x.get_location()):
                killed.add(x)
                model.remove(x)
        return killed
    
    def display(self, canvas):
        coordinate = self.get_location()
        canvas.create_oval(coordinate[0]-Special.radius, coordinate[1]-Special.radius,
                                coordinate[0]+Special.radius, coordinate[1]+Special.radius,
                                fill='green')
    
    def contains(self, xy):
        return Mobile_Simulton.contains(self, xy)