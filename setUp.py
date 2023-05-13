from MDP import MDP
from FinalVersion.parser import parse_file

def setUp_mdpSolver(file):
    # Parse the input file
    states, actions, inm_costs, transitions = parse_file(file)

    # Initialize the MDP object
    my_mdp = MDP(states, transitions, actions, inm_costs)

    return my_mdp


###################################
'''
# Specific example initialization -> ... -> mdp initialization

# Initialization of individual states
s1 = State(16, 0)
s2 = State(16.5, 0)
s3 = State(17, 0)
s4 = State(17.5, 0)
s5 = State(18, 0)
s6 = State(18.5, 0)
s7 = State(19, 0)
s8 = State(19.5, 0)
s9 = State(20, 0)
s10 = State(20.5, 0)
s11 = State(21, 0)
s12 = State(21.5, 0)
s13 = State(22, 1)
s14 = State(22.5, 0)
s15 = State(23, 0)
s16 = State(23.5, 0)
s17 = State(24, 0)
s18 = State(24.5, 0)
s19 = State(25, 0)

# Initialization of set of states
S = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19}

# Initialization of individual actions
a1 = Action('on')
a2 = Action('off')

# Initialization of set of actions
A = {a1, a2}

# Initialization of individual transitions
t1 = Transition(s1, s1, a1)
t2 = Transition(s1, s1, a2)
t3 = Transition(s1, s2, a1)
t4 = Transition(s1, s2, a2)
t5 = Transition(s1, s3, a1)
t6 = Transition(s2, s1, a1)
t7 = Transition(s2, s1, a2)
t8 = Transition(s2, s3, a1)
t9 = Transition(s2, s3, a2)
t10 = Transition(s2, s1, a2)
t11 = Transition(s2, s2, a2)
t12 = Transition(s2, s3, a2)
t13 = Transition(s3, s1, a1)
t14 = Transition(s3, s2, a1)
t15 = Transition(s3, s3, a1)
t16 = Transition(s3, s1, a2)
t17 = Transition(s3, s2, a2)
t18 = Transition(s3, s3, a2)

# Initialization of dictionary of transitions
T = {t1: 0.2, t2: 0.6, t3: 0.2, t4: 0.0, t5: 0.2, t6: 0.8, t7: 0.1, t8: 0.7, t9: 0.2, t10: 0.0, t11: 0.2, t12: 0.8,
     t13: 0.1, t14: 0.0, t15: 0.9, t16: 0.9, t17: 0.0, t18: 0.1}  # transition model

# Initialize dictionary of immediate costs
IC = {a1: 5, a2: 2}

# Initialization of my_mdp object
my_mdp = MDP(S, T, A, IC)

my_mdp.PrintAll()

Values = my_mdp.ValueIteration()
for i in Values:
    print(str(i) + " = " + str(Values[i]))'''
