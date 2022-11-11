import itertools
players = dict()
rank = dict()

for i in range(5):
    name = input()
    preferences = list(map(int, input().split()))
    name2 = input()
    preferences2 = list(map(int, input().split()))
    rank[i] = (name, name2)
    players[name] = dict()
    players[name2] = dict()
    for j in range(5):
        players[name][preferences[j]] = j 
        players[name2][preferences2[j]] = j 


def rec(increment, team1, team2):
    if increment < 5:
        v1t1 = list(team1)
        v1t2 = list(team2)
        v1t1.append(rank[increment][0])
        v1t2.append(rank[increment][1])
        v1 = rec(increment+1, v1t1, v1t2)
        v2t1 = list(team1)
        v2t2 = list(team2)
        v2t1.append(rank[increment][1])
        v2t2.append(rank[increment][0])
        v2 = rec(increment+1, v2t1, v2t2)
        if v1[0]-v1[3] > v2[0]-v2[3]:
            return v1
        else:
            return v2

    else:
        perm1 = itertools.permutations(team1)
        perm2 = itertools.permutations(team2)
        print("Team1:")
        best_team1 = best_team(perm1)
        print("Team2:")
        best_team2 = best_team(perm2)
        if best_team1[0] > best_team2[0]:
            return (best_team1[0], best_team1[1], best_team2[1], abs(best_team1[0]-best_team2[0]))
        else:
            return (best_team2[0], best_team1[1], best_team2[1], abs(best_team1[0]-best_team2[0]))






def best_role(name, picked):
    if picked[players[name][5]][0] != True:
        picked[players[name][5]] = (True, name)
        return 5
        
        
    elif picked[players[name][4]][0] != True: 
        picked[players[name][4]] = (True, name)
        return 4
        
    elif picked[players[name][3]][0] != True: 
        picked[players[name][3]] = (True, name)
        return 3

    elif picked[players[name][2]][0] != True: 
        picked[players[name][2]] = (True, name)
        return 2

    else: 
        picked[players[name][1]] = (True, name)
        return 1 
 


def best_team(permutations):
    max = 0
    best_team = [""]*5
    for t in permutations:
        current = 0
        picked = {0: (False, ""), 1: (False, ""), 2: (False, ""), 3: (False, ""), 4: (False, "")}
        for i in range(5):
            current += best_role(t[i], picked)
        
        if current > max: 
            max = current
            for i in range(5):
                best_team[i] = picked[i][1]

    print(max)
    print()
    print("Top: ", best_team[0])
    print("Jun: ", best_team[1])
    print("Mid: ", best_team[2])
    print("ADC: ", best_team[3])
    print("Sup: ", best_team[4])
    print()
    print()
   
    return (max, best_team)


t1 = []
t2 = []

t1.append(rank[0][0])
t2.append(rank[0][1])

best_teams = rec(1, t1, t2)

print()
print()
print("Team 1:")
print("Top: ", best_teams[1][0])
print("Jun: ", best_teams[1][1])
print("Mid: ", best_teams[1][2])
print("ADC: ", best_teams[1][3])
print("Sup: ", best_teams[1][4])

print()
print()
print("Team 2:")
print("Top: ", best_teams[2][0])
print("Jun: ", best_teams[2][1])
print("Mid: ", best_teams[2][2])
print("ADC: ", best_teams[2][3])
print("Sup: ", best_teams[2][4])
print()
print()
#print(best_teams[0], best_teams[1], best_teams[2], best_teams[3])