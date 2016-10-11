# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter_constant = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = Pulsator.counter_constant

    def update(self):
        remove_simultons =  Black_Hole.contains(self)
        if len(remove_simultons) == 0:
            self.counter -= 1
            if self.counter == 0:
                Black_Hole.change_dimension(self, -1, -1)
                self.counter = Pulsator.counter_constant
        elif len(remove_simultons) > 0:
            size_change = len(remove_simultons)
            Black_Hole.change_dimension(self, size_change, size_change)
            self.counter = Pulsator.counter_constant
        return remove_simultons

