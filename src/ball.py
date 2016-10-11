# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 5, 5, 0, 5)
        Prey.randomize_angle(self)

    def update(self):
        Prey.move(self)

    def display(self, canvas):
        _x, _y = Prey.get_location(self)
        canvas.create_oval(_x-Ball.radius, _y-Ball.radius,
                                _x+Ball.radius, _y+Ball.radius,
                                fill='blue')
