import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Splitter as Special, Splitter_Minion
from simulton import Simulton
from collections import defaultdict


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
step = False
cycle_count = 0
simultons = set()
current_object = 'Ball'


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons
    running     = False;
    cycle_count = 0;
    simultons       = set()


#start running the simulation
def start ():
    global running
    if len(simultons) != 0:
        running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global step
    step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global current_object
    current_object = kind
    print(current_object)


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    result = current_object + '(' + str(x) + ',' + str(y) + ')'
    if current_object != 'Remove':
        return add(eval(result))
    elif current_object == 'Remove':
        remove_simulatons = set()
        for b in simultons:
            xy = (x, y)
            if Simulton.contains(b, xy):
                remove_simulatons.add(b)
        for item in remove_simulatons:
            remove(item)

#add simulton s to the simulation
def add(s):
    simultons.add(s)


# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for item in simultons:
        if p(item):
            result.add(item)
    return result

#call update for every simulton in the simulation
def update_all():
    global cycle_count
    global step
    global simultons

    remove_simultons = set()
    add_simultons = defaultdict(int)
    if step or running:
        cycle_count += 1
        for b in simultons:
            if isinstance(b, Special):
                for item in b.update():
                    if item != b:
                        remove_simultons.add(item)
                        add_simultons[b] += 1
            elif isinstance(b, Black_Hole):
                for item in b.update():
                    if item != b:
                        remove_simultons.add(item)
            else:
                b.update()
        step = False
    for b in simultons:
        if isinstance(b, Black_Hole) and b.get_dimension() == (0, 0):
            remove_simultons.add(b)
    for item in remove_simultons:
        simultons.remove(item)
    for b, value in add_simultons.items():
        _x, _y = b.get_location()
        for _ in range(value):
            add(Splitter_Minion(_x, _y))


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)

    for b in simultons:
        b.display(controller.the_canvas)

    controller.the_progress.config(text=str(len(simultons))+" balls/"+str(cycle_count)+" cycles")
