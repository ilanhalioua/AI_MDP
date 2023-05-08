COST_ON = 0.0455 # euros. Search cost electricity per half hour
COST_OFF = 0.0455 # euros
GOAL = 22

def value_iteration(S, A, P, C):
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
            V[GOAL] = 0
            optimal_policy[s] = min(Q, key=Q.get)
            optimal_policy[GOAL] = "Not Defined"
        if all(oldV[s] == V[s] for s in S):
            break

    return V, optimal_policy


S = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25] # [16, 16.5, ..., 24.5, 25]
A = [1, 0] # [On, Off]

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


def C(a):
    if a == 1:
        c = COST_ON
    elif a == 0:
        c = COST_OFF

    return c

V, optimalPolicy = value_iteration(S, A, P, C)

print("V = " + str(V))
print("optimal_policy = " + str(optimalPolicy))