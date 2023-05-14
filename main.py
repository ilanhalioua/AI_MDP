from setUp import setUp_mdpSolver

file = input("Introduce name of file that contains your MDP problem: ")
basic_mdp = setUp_mdpSolver(file)
V = basic_mdp.ValueIteration()
policy = basic_mdp.OptimalPolicy(V)

# Print the resulting policy
for state in policy:
    print(f"State: {state}, Action: {policy[state]}")
