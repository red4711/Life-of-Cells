# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
import model
from prey import Prey
from math import atan2



class Hunter(Pulsator, Mobile_Simulton):
    hunt_radius = 200
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, 5, 5, 0, 5)
        Pulsator.__init__(self, x, y)
        self.randomize_angle()

    def update(self):
        current_target = (None, Hunter.hunt_radius + 1)
        for item in model.find(lambda x: isinstance(x, Prey)):
            target_distance = Mobile_Simulton.distance(self, item.get_location())
            if target_distance < Hunter.hunt_radius and target_distance < current_target[1]:
                current_target = (item, target_distance)

        if current_target[0] is not None:
            target_x, target_y = current_target[0].get_location()
            x, y = Mobile_Simulton.get_location(self)
            dy = target_y - y
            dx = target_x - x
            self._angle = atan2(dy, dx)

        Mobile_Simulton.move(self)
        return Pulsator.update(self)



