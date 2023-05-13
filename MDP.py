class State:
    def __init__(self, val):
        self.state_val = val

class Action:
    def __init__(self, name):
        self.action_name = name

class Transition:
    def __init__(self, p:State, q:State, a:Action, P):
        self.state_from = p
        self.state_to = q
        self.through = a
        self.prob = P

class Cost:
    def __init__(self, s:State, a:Action, C):
        self.through = a
        self.state_from = s
        self.cost = C

class ImmediateCost:
    def __init__(self, a: Action, ic):
        self.through = a
        self.imm_cost = ic



class MDP:
    def __init__(self, S:[State], T:[Transition], A:[Action], C:[Cost]): # Use set type instead of array/list
        self.States = S #set of state objects
        self.Transitions = T #set of transition objects
        self.Actions = A # set of action objects
        self.Costs = C # set of cost objects

    def file_init(self, fileName: str):
        ...# Complete this bing chat



def ValueIteration(m: MDP):
    # Initialize mdp problem
        # Initialice set of states
        States = {for s in S} # S filled by file lecture
        # Initialice set of transitions
        # Initialice set of actions
        # Initialice set of costs

    mdp = MDP(23,232,3232)





