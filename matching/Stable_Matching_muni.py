from collections import defaultdict

def inputcommand():
    i = input()
    if i.startswith("#"):
        return inputcommand()
    return i



n = int(inputcommand().split("=")[1])

id_people = dict()
people_id = dict()

for _ in range(n*2):
    il = input().split()
    id_people[int(il[0])] = il[1]

input()

rankings = dict()

for _ in range(n*2):
    strl = input().split(": ")
    pref = map(int, strl[1].split(" "))
    if int(strl[0]) % 2 == 0:
        tmp = dict()
        for i, m in enumerate(pref):
            tmp[m] = i
        rankings[int(strl[0])] = tmp
    else:
        rankings[int(strl[0])] = list(pref)

suiters = set([i*2 + 1 for i in range(n)])
matches = defaultdict(lambda : None)


while suiters:
    m = suiters.pop()
    w = rankings[m].pop(0)
    if matches[w]:
        if rankings[w][matches[w]] > rankings[w][m]:
            suiters.add(matches[w])
            matches[w] = m
            matches[m] = w
        else:
            suiters.add(m)
    else:
        matches[w] = m
        matches[m] = w


[print(id_people[i * 2 + 1], "--", id_people[matches[i * 2 + 1]]) for i in range(n)]
    
    



