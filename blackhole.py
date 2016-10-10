# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 10, 10)

    def update(self):
        return self.contains()

    def display(self, canvas):
        _x, _y = self.get_location()
        x_radius, y_radius = self.get_dimension()
        canvas.create_oval(_x-x_radius, _y-y_radius,
                                _x+x_radius, _y+y_radius,
                                fill='black')

    def contains(self):
        result = set()
        for item in model.find(lambda x: isinstance(x, Prey)):
            if Simulton.contains(self, Simulton.get_location(item)):
                result.add(item)
        return result