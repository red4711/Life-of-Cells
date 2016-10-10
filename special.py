#Splitter is a sub class of Hunter
#For each prey it eats, it spawns 1 Minion which
#is a Black Hole that moves in a straight line


from hunter import Hunter

from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton

class Splitter(Hunter):
    display_radius = 15
    def __init__(self, x, y):
        Hunter.__init__(self, x, y)
        self.randomize_angle()

    def display(self, canvas):
        _x, _y = self.get_location()
        canvas.create_oval(_x-Splitter.display_radius, _y-Splitter.display_radius,
                                _x+Splitter.display_radius, _y+Splitter.display_radius,
                                fill='purple')

class Splitter_Minion(Black_Hole, Mobile_Simulton):
    radius = 10
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 10, 10, 10, 5)
        self.randomize_angle()

    def update(self):
        Mobile_Simulton.move(self)
        return Black_Hole.update(self)


    def display(self, canvas):
        _x, _y = self.get_location()
        canvas.create_oval(_x-Splitter_Minion.radius, _y-Splitter_Minion.radius,
                                _x+Splitter_Minion.radius, _y+Splitter_Minion.radius,
                                fill='pink')
