
def inputReader():
    i = input()
    if i.startswith("#"):
        return inputReader()
    else:
        return i


n = int(inputReader().split("=")[1])

persons = dict()
preferences = dict()

##### cost N #####
for _ in range(n*2):
    number_name = input().split(" ")
    persons[int(number_name[0])] = number_name[1]

input()


##### cost for men: N #####
##### cost for women: N^2 #####

for _ in range(n*2):
    number_pref = input().split(": ")
    if int(number_pref[0]) % 2 == 1:
        preferences[int(number_pref[0])] = number_pref[1].split(" ")
    else:
        preferences[int(number_pref[0])] = dict()
        pref_order = number_pref[1].split(" ")
        for i in range(n):
            preferences[int(number_pref[0])][int(pref_order[i])] = i


P = set([i*2+1 for i in range(n)])
matches = dict()

while P:
    man = int(P.pop())
    woman = int(preferences[man].pop(0))
    if woman in matches:
        if preferences[woman][matches[woman]] > preferences[woman][man]:
            P.add(matches[woman])
            matches[woman] = man
            matches[man] = woman
        else:
            P.add(man)
    else:
        matches[woman] = man
        matches[man] = woman

for i in range(n):
    print(persons[i*2+1] + " -- " + persons[matches[i*2+1]])
