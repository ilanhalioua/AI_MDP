from setUp import setUp_mdpSolver, askFile

file = askFile()
user_mdp = setUp_mdpSolver(file)
if user_mdp.States and user_mdp.Actions and user_mdp.Transitions and user_mdp.ImmediateCosts:
    V = user_mdp.ValueIteration()
    policy = user_mdp.OptimalPolicy(V)
    user_mdp.WriteOptimalPolicy(policy)

    # Print the Value function for each state
    print("\nValue function for each state:\n")
    for state in V:
        print(f"V( {state} ) = {V[state]}")

    # Print the resulting policy
    print("\n\nOptimal Policy:\n")
    for state in policy:
        print(f"{state} -> Optimal: {policy[state]}")

else:
    print("\nIntroduce your mdp definition with the expected file format, please!")
