from MDP import State, Action, Transition
import re


def parse_file(file):
    # Initialize the list of transitions
    states = set()
    actions = set()
    transitions = {}
    goal_S = 0
    goal_T = 0

    # Open the input file
    with open(file, 'r') as f:
        # Read the file line by line
        for line in f:
            # Match the line that starts with "states:"
            if line.lower().startswith('states:'):
                # print()
                # Use regular expressions to find all states in the line
                matches = re.findall(r'([\w.]+(?:)?\*?)', line)[1:] # match one or more word characters or periods (user may introduce states with ‘decimal’ format as in our thermostat problem), optionally followed by an asterisk (which will serve as a flag for the goal state).
                for match in matches:
                    # Create a State object for each state found
                    val = match.rstrip('*')
                    g = 1 if match.endswith('*') else 0
                    if g == 1:
                        goal_S = 1
                    state = State(val, g)
                    # print(state)
                    states.add(state)
                # print("S = " + str(states))
                if goal_S != 1:
                    print("\nGoal state was not introduced in <States line>.\nPlease use the flag * after inserting a goal state.\ne.g.: States: s1, s2, s3*, s4")
            # Match the line that starts with "actions:"
            elif line.lower().startswith('actions:'):
                # print()
                # Extract the list of actions
                action_names = re.findall(r'\b[\w.]+\b', line)[1:] # match whole words consisting of word characters or periods
                for name in action_names:
                    action = Action(name)
                    # print(action)
                    actions.add(action)
                # print("A = " + str(actions))
            # Match the line that starts with "costs:"
            elif line.lower().startswith('costs:'):
                # print()
                # Extract the costs
                costs = re.findall(r'c\(\s*([\w.]+)\)\s*=\s*(\d+(?:\.\d+)?)', line) # match a cost expression in the form of 'c(name) = value', where 'name' represents the cost name (composed of word characters or periods) and 'value' represents the cost value (a numeric value)
                # Convert the costs to a dictionary
                costs = {Action(action): float(cost) for action, cost in costs}
                # print("IC = " + str(costs))
            # Match the lines that start with "transitions:"
            elif line.lower().startswith('transitions:'):
                # print()
                matches = re.findall(r'T\(\s*([\w.]+(?:)?\*?),\s*([\w.]+(?:)?\*?),\s*([\w.]+)\)\s*=\s(\d+(?:\.\d+)?)', line) # match a transitions and their respective probabilities when found in the form of 'T(name1, name2, name3) = value', where 'name1', 'name2', and 'name3' represent the parameters (composed of word characters or periods) and 'value' represents the numeric value (probability) assigned to the transition.
                for match in matches:
                    p_val = match[0].rstrip('*')
                    p_goal = 1 if match[0].endswith('*') else 0
                    p = State(p_val, p_goal)

                    q_val = match[1].rstrip('*')
                    q_goal = 1 if match[1].endswith('*') else 0
                    q = State(q_val, q_goal)

                    if p_goal == 1 or q_goal == 1:
                        goal_T = 1

                    a_name = match[2]
                    a = Action(a_name)

                    prob = float(match[3])
                    transition = Transition(p, q, a)
                    # print(transition)

                    transitions[transition] = prob
                # print("T = " + str(transitions))
                if goal_T != 1:
                    print("\nGoal state was not introduced in <Transition line>.\nPlease use the flag * after inserting a goal state.\ne.g.: Transitions: T(s1,s1,act1) = 0.3, T(s1,s2*,act2) = 0.9")
                    print("\nAlso, check that the goal states introduced in the transitions line are the same as the ones in the states line!")

    if goal_S != 0 and goal_T != 0:
        return states, actions, costs, transitions
    else:
        return None, None, None, None
