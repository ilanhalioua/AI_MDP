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
                # Use regular expressions to find all states in the line
                goal = float(re.search(r'(\d+(?:\.\d+)?)\*', line).group(1))
                matches = re.findall(r'(\d+\*?)', line)
                for match in matches:
                    # Create a State object for each state found
                    val = int(match.rstrip('*'))
                    g = 1 if match.endswith('*') else 0
                    state = State(val, g)
                    print(state)
                    states.add(state)
                print(states)
            # Match the line that starts with "actions:"
            elif line.startswith('actions:'):
                # Extract the list of actions
                action_names = re.findall(r'\b\w+\b', line)[1:]
                for name in action_names:
                    action = Action(name)
                    print(action)
                    actions.add(action)
                print(actions)
            # Match the line that starts with "costs:"
            elif line.startswith('costs:'):
                # Extract the costs
                costs = re.findall(r'c\((\w+)\) = (\d+(?:\.\d+)?)', line)
                # Convert the costs to a dictionary
                costs = {action: float(cost) for action, cost in costs}
                print(costs)
            # Match the lines that start with "transitions:"
            elif line.startswith('transitions:'):
                matches = re.findall(r'T\((\d+),(\d+),(\w)\) = (\d\.\d)', line)
                for match in matches:
                    if match[0] or match[1] == goal:
                        g = 1
                    else:
                        g = 0
                    p = State(match[0], g)
                    q = State(match[1], g)
                    a = Action(match[2])
                    prob = float(match[3])
                    transition = Transition(p, q, a)
                    print(transition)
                    transitions[transition] = prob
                print(transitions)

    return states, actions, costs, transitions

# Un-comment the line below and run this file if you want to check what the parser is doing 
# states, actions, costs, transitions = parse_file('file')
