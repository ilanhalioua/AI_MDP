import re

# Open the input file
with open('file', 'r') as f:
    # Read the file line by line
    for line in f:
        # Match the line that starts with "states:"
        if line.startswith('states:'):
            # Extract the list of states
            states = list(map(float, re.findall(r'\b\d+(?:\.\d+)?\b', line)))
            print(states)
            # Extract the goal state
            goal = float(re.search(r'(\d+(?:\.\d+)?)\*', line).group(1))
            print(goal)
        # Match the line that starts with "actions:"
        elif line.startswith('actions:'):
            # Extract the list of actions
            actions = re.findall(r'\b\w+\b', line)[1:]
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
            # Extract the transitions
            transitions = re.findall(r'T\((\d+(?:\.\d+)?), (\d+(?:\.\d+)?), (\w+), (\d+(?:\.\d+)?)\)', line)
            # Convert the transitions to a list of tuples
            transitions = [(float(s1), float(s2), a, float(p)) for s1, s2, a, p in transitions]
            print(transitions)

'''
#COST_ON = 0.2 # euros. Search cost electricity per half hour
#COST_OFF = 0.0455 # euros

def value_iteration(S, goal, A, P, C):
    V = {s: 0 for s in S}
    optimal_policy = {s: 0 for s in S}
    while True:
        oldV = V.copy()

        for s in S:
            Q = {}
            for a in A:
                Q[a] = C(a) + sum(P(s_next,s,a) * oldV[s_next]
                                  for s_next in S)
            V[s] = min(Q.values())
            V[goal] = 0
            optimal_policy[s] = min(Q, key=Q.get)
            optimal_policy[goal] = "Not Defined"
        if all(oldV[s] == V[s] for s in S):
            break

    return V, optimal_policy

def P(s_next, s, a):
    if a == 1:
        if 16.5 <= s <= 21.5 or 22.5 <= s <= 24:
            if s_next == s + 0.5:
                p = 0.5
            elif s_next == s + 1:
                p = 0.2
            elif s_next == s:
                p = 0.2
            elif s_next == s - 0.5:
                p = 0.1
            else:
                p = 0
        elif s == 16:
            if s_next == s + 0.5:
                p = 0.5
            elif s_next == s + 1:
                p = 0.2
            elif s_next == s:
                p = 0.3
            else:
                p = 0
        elif s == 22:
            p = 0
        elif s == 24.5:
            if s_next == s + 0.5:
                p = 0.7
            elif s_next == s:
                p = 0.2
            elif s_next == s - 0.5:
                p = 0.1
            else:
                p = 0
        elif s == 25:
            if s_next == s:
                p = 0.9
            elif s_next == s - 0.5:
                p = 0.1
            else:
                p = 0
    elif a == 0:
        if 16.5 <= s <= 21.5 or 22.5 <= s <= 24.5:
            if s_next == s - 0.5:
                p = 0.7
            elif s_next == s:
                p = 0.2
            elif s_next == s + 0.5:
                p = 0.1
            else:
                p = 0
        elif s == 16:
            if s_next == s:
                p = 0.9
            elif s_next == s + 0.5:
                p = 0.1
            else:
                p = 0
        elif s == 22:
            p = 0
        elif s == 25:
            if s_next == s - 0.5:
                p = 0.7
            elif s_next == s:
                p = 0.3
            else:
                p = 0
    return p


def C(a): # a is a dictionary
    if a == 1:
        c = COST_ON
    elif a == 0:
        c = COST_OFF

    if a == 

    return c

V, optimalPolicy = value_iteration(states, goal, actions, probabilities, costs)

print("V = " + str(V))
print("optimal_policy = " + str(optimalPolicy))
'''