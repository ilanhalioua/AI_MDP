from MDP import State, Action, Transition
import re

def parse_file(file):
    # Initialize the list of transitions
    states = set()
    actions = set()
    transitions = {}

    # Open the input file
    with open(file, 'r') as f:
        # Read the file line by line
        for line in f:
            # Match the line that starts with "states:"
            if line.startswith('states:'):
                # print()
                # Use regular expressions to find all states in the line
                matches = re.findall(r'(\d+(?:\.\d+)?\*?)', line)
                for match in matches:
                    # Create a State object for each state found
                    val = float(match.rstrip('*'))
                    g = 1 if match.endswith('*') else 0
                    state = State(val, g)
                    # print(state)
                    states.add(state)
                # print("S = " + str(states))
            # Match the line that starts with "actions:"
            elif line.startswith('actions:'):
                # print()
                # Extract the list of actions
                action_names = re.findall(r'\b\w+\b', line)[1:]
                for name in action_names:
                    action = Action(name)
                    # print(action)
                    actions.add(action)
                # print("A = " + str(actions))
            # Match the line that starts with "costs:"
            elif line.startswith('costs:'):
                # print()
                # Extract the costs
                costs = re.findall(r'c\((\w+)\) = (\d+(?:\.\d+)?)', line)
                # Convert the costs to a dictionary
                costs = {Action(action): float(cost) for action, cost in costs}
                # print("IC = " + str(costs))
            # Match the lines that start with "transitions:"
            elif line.startswith('transitions:'):
                # print()
                matches = re.findall(r'T\((\d+(?:\.\d+)?\*?),(\d+(?:\.\d+)?\*?),(\w+)\) = (\d+(?:\.\d+)?)', line)
                for match in matches:
                    p_val = float(match[0].rstrip('*'))
                    p_goal = 1 if match[0].endswith('*') else 0
                    p = State(p_val, p_goal)

                    q_val = float(match[1].rstrip('*'))
                    q_goal = 1 if match[1].endswith('*') else 0
                    q = State(q_val, q_goal)

                    a_name = match[2]
                    a = Action(a_name)

                    prob = float(match[3])
                    transition = Transition(p, q, a)
                    # print(transition)

                    transitions[transition] = prob
                # print("T = " + str(transitions))

    return states, actions, costs, transitions

# Un-comment the line below and run this file if you want to check what the parser is doing 
# states, actions, costs, transitions = parse_file('file')
