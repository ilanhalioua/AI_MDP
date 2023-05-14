import os
from MDP import MDP
from parser import parse_file

def askFile():
    while True:
        file = input("Enter the name of the file that contains your MDP problem: ")
        if file == 'STOP' or os.path.isfile(file):
            return file
            break
        else:
            print("File not found. Please try again.\n")

def setUp_mdpSolver(file):
    # Parse the input file
    states, actions, inm_costs, transitions = parse_file(file)

    # Initialize the MDP object
    my_mdp = MDP(states, transitions, actions, inm_costs)

    return my_mdp
