# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 5, 5, 0, 5)
        Prey.randomize_angle(self)

    def update(self):
        if random() <= 0.3:
            # new_speed = 0
            # if 3 < Prey.get_speed(self) < 7:
            #     while new_speed < 0:
            #         new_speed = (random() - .5) + Prey.get_speed(self)
            # else:
            #     new_speed = (random() - .5) + Prey.get_speed(self)
            # Prey.set_velocity(self, new_speed, (random() - .5) + Prey.get_angle(self))

            random_float = random()
            if 3 < Prey.get_speed(self) + (random_float - .5) < 7:
                Prey.set_velocity(self, Prey.get_speed(self) + (random_float - .5), (random() - .5) + Prey.get_angle(self))
            else:
                # Prey.set_velocity(self, Prey.get_speed(self) + (random_float / 2), (random() - .5) + Prey.get_angle(self))
                Prey.set_velocity(self, Prey.get_speed(self) - (random_float - .5), (random() - .5) + Prey.get_angle(self))
        Prey.move(self)

    def display(self, canvas):
        _x, _y = Prey.get_location(self)
        canvas.create_oval(_x-Floater.radius, _y-Floater.radius,
                                _x+Floater.radius, _y+Floater.radius,
                                fill='red')