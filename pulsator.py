# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    time_betw_meal = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self._counter = 0
    def update(self, model):
        self._counter += 1
        eaten = Black_Hole.update(self, model)
        if len(eaten) == 0:
            if self._counter == 30:
                self.change_dimension(-1, -1)
                self._counter = 0
                if 0 in self.get_dimension():
                    model.remove(self)
        else:
            self._counter = 0
            for x in eaten:
                self.change_dimension(1, 1)
        return eaten 
                
    
