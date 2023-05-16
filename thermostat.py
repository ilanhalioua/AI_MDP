from setUp import setUp_mdpSolver
from MDP import State, Transition, Action, MDP

###############################################################
#                                                             #
#  This python file was done during the process and was used  #
#  to try the thermostat problem before creating the parser.  #
#  ---------------------- EXTRA ----------------------------  #
#                                                             #
###############################################################


def Thermostat():
    # declare and define the set of states with 22 as a goal state
    S =set()
    temps = [x / 2 for x in range(32, 51)]
    for i in temps:
        if i == 22.0:
            S.add(State(i, 1))
        else:
            S.add(State(i, 0))
    # declare and define the set of actions (on and off)
    A = set()
    A.add(Action("on"))
    A.add(Action("off"))
    # declare and define the immediate costs of these actions
    Ic = { Action("on"): 5000.0, Action("off"): 40.0}
    # declare and define the transition model ie: transitions <-> probability
    #when turning the heating on...
    T = {}
    a = Action("on")
    for i in temps:
        if i == 16.0:
            # stays the same for p = 0.3, up by0.5 with p=0.5 and up by 1 with p = 0.2
            T[Transition(State(i, 0), State(i, 0), a)] = 0.3
            T[Transition(State(i, 0), State(i+0.5, 0), a)] = 0.5
            T[Transition(State(i, 0), State(i+1, 0), a)] = 0.2

        elif i == 25.0:
            # goes down BY 0.5?! with p = 0.1 and stays the same with p=0.9
            T[Transition(State(i, 0), State(i-0.5, 0), a)] = 0.1
            T[Transition(State(i, 0), State(i, 0), a)] = 0.9
        elif i == 24.5:
            # goes up by 0.5 with p = 0.7 and stays the same with p = 0.3
            T[Transition(State(i, 0), State(i+0.5, 0), a)] = 0.7
            T[Transition(State(i, 0), State(i, 0), a)] = 0.3
        else:
            if i != 22.0: # not goal
                # rises by 0.5 with p = 0.5 , rises by 1.0 with p = 0.2 , stays the same for p = 0.2 and falls by 0.5 with p = 0.1
                if i+0.5 != 22.0:
                    T[Transition(State(i, 0), State(i, 0), a)] = 0.2
                    T[Transition(State(i, 0), State(i+0.5, 0), a)] = 0.5
                    if i + 1.0 != 22.0:
                        T[Transition(State(i, 0), State(i + 1.0, 0), a)] = 0.2
                        if i - 0.5 != 22.0:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                        else:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                    else:
                        T[Transition(State(i, 0), State(i + 1.0, 1), a)] = 0.2
                        if i - 0.5 != 22.0:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                        else:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                else:
                    T[Transition(State(i, 1), State(i, 1), a)] = 0.2
                    T[Transition(State(i, 0), State(i+0.5, 1), a)] = 0.5
                    if i + 1.0 != 22.0:
                        T[Transition(State(i, 0), State(i + 1.0, 0), a)] = 0.2
                        if i - 0.5 != 22.0:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                        else:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                    else:
                        T[Transition(State(i, 0), State(i + 1.0, 1), a)] = 0.2
                        if i - 0.5 != 22.0:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
                        else:
                            T[Transition(State(i, 0), State(i - 0.5, 0), a)] = 0.1
            else:
                T[Transition(State(i, 1), State(i + 0.5, 0), a)] = 0.5
                T[Transition(State(i, 1), State(i + 1.0, 0), a)] = 0.2
                T[Transition(State(i, 1), State(i, 1), a)] = 0.2
                T[Transition(State(i, 1), State(i - 0.5, 0), a)] = 0.1

    # now, when turining the heat off...
    b = Action("off")
    for i in temps:
        if i == 16.0:
            #stays the same with p = 0.9 ...
            T[Transition(State(i, 0), State(i, 0), b)] = 0.9
            T[Transition(State(i, 0), State(i+0.5, 0), b)] = 0.1
        elif i == 25.0:
            #stays the same with p = 0.
            T[Transition(State(i, 0), State(i, 0), b)] = 0.3
            T[Transition(State(i, 0), State(i-0.5, 0), b)] = 0.7
        elif i != 22.0:

            # goes down by 0.5 with p = 0.7, up 0.5  with p = 0.1 and stays the same with p = 0.2
            if i-0.5 != 22.0:
                T[Transition(State(i, 0), State(i, 0), b)] = 0.2
                T[Transition(State(i, 0), State(i-0.5, 0), b)] = 0.7
                if i+0.5 != 22.0:
                    T[Transition(State(i, 0), State(i+0.5, 0), b)] = 0.1
                else:
                    T[Transition(State(i, 0), State(i+0.5, 1), b)] = 0.1

            else:
                T[Transition(State(i, 0), State(i, 0), b)] = 0.2
                T[Transition(State(i, 0), State(i-0.5, 1), b)] = 0.7
                if i + 0.5 != 22.0:
                    T[Transition(State(i, 0), State(i + 0.5, 0), b)] = 0.1
                else:
                    T[Transition(State(i, 0), State(i + 0.5, 1), b)] = 0.1
        else:
            T[Transition(State(i, 1), State(i - 0.5, 0), b)] = 0.7
            T[Transition(State(i, 1), State(i + 0.5, 1), b)] = 0.1
            T[Transition(State(i, 1), State(i, 1), b)] = 0.2

    return MDP(S, T, A, Ic)


#testing this function:
Thermostat_mdp = Thermostat()
Thermostat_mdp.PrintAll()
print("Transition space size -> "+ str(len(Thermostat_mdp.Transitions)))
print("State set size -> " + str(len(Thermostat_mdp.States)))
print("Action set size -> " + str(len(Thermostat_mdp.Actions)))

print("\nV[state] for the smart thermostat agent is given below : ")
Vi = Thermostat_mdp.ValueIteration()
for v in Vi:
    print(str(v) + " = " + str(Vi[v]))
print()


print("Optimal policy for the smart thermostat agent is given below : ")
Pi = Thermostat_mdp.OptimalPolicy()
for s in Pi:
    print(str(s) + " = " + str(Pi[s]))
