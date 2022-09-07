def input_command():
    i = input()
    if i.startswith("#"):
        return input_command()
    return i

n = int(input_command().split("=")[1])

id_people = dict()

##### cost N #####
for _ in range(n*2):
    number_name = input().split(" ")
    id_people[int(number_name[0])] = number_name[1]

input()

rankings = dict()

##### cost for men: N #####
##### cost for women: N^2 #####

for _ in range(n*2):
    number_pref = input().split(": ")
    if int(number_pref[0]) % 2 == 0:
        rankings[int(number_pref[0])] = dict()
        pref_order = number_pref[1].split(" ")
        for i in range(n):
            rankings[int(number_pref[0])][int(pref_order[i])] = i
    else:
        rankings[int(number_pref[0])] = number_pref[1].split(" ")

suiters = set([i*2 + 1 for i in range(n)])
matches = dict()


while suiters:
    m = int(suiters.pop())
    w = int(rankings[m].pop(0))
    if w in matches:
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

