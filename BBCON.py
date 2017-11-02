class BBCON():

    behaviors #a list of all the behavior objects used by the bbcon
    active-behaviors #a list of all behaviors that are currently active.
    sensobs #a list of all sensory objects used by the bbcon
    motobs #a list of all motor objects used by the bbcon
    arbitrator #the arbitrator object that will resolve actuator requests produced by the behaviors.

    #Other instance variables, such as the current timestep, the inactive behaviors, and the controlled agent/robot
    #may also prove useful in your implementation.

    add behavior #append a newly-created behavior onto the behaviors list.
    add sensob #append a newly-created sensob onto the sensobs list.
    activate behavior #add an existing behavior onto the active-behaviors list.
    deactive behavior #remove an existing behavior from the active behaviors list.
