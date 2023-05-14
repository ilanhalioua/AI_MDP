from setUp import setUp_mdpSolver

file = input("Introduce name of file that contains your MDP problem: ")
basic_mdp = setUp_mdpSolver(file)
V = basic_mdp.ValueIteration()
policy = basic_mdp.OptimalPolicy(V)

# Print the Value function for each state
print("\nValue function for each state:\n")
for state in V:
    print(f"V( {state} ) = {V[state]}")

# Print the resulting policy
print("\n\nOptimal Policy:\n")
for state in policy:
    print(f"{state} -> Optimal: {policy[state]}")
