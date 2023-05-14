from MDP import MDP
from parser import parse_file

def setUp_mdpSolver(file):
    # Parse the input file
    states, actions, inm_costs, transitions = parse_file(file)

    # Initialize the MDP object
    my_mdp = MDP(states, transitions, actions, inm_costs)

    return my_mdp

