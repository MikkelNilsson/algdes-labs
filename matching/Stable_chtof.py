def inputReader():
    i = input()
    if i.startswith("#"):
        return inputReader()
    else: 
        return i

n = int(inputReader().split("=")[1])

p = dict()
pref = dict()

for _ in range (n*2):
    numname = input().split(" ")
    p[int(numname[0])] = numname[1]

input()

for _ in range(n*2):
    numpref = input().split(": ")
    if int(numpref[0]) % 2 == 1:
        pref[int(numpref[0])] = numpref[1].split(" ")
    else: 
        pref[int(numpref[0])] = dict()
        order = numpref[1].split(" ")
        for i in range(n):
            pref[int(numpref[0])][int(order[i])] = i



P = set([i*2+1 for i in range(n)]) 
match = dict()

while P:
    man = int(P.pop())
    woman = int(pref[man].pop(0))
    if woman in match:
        if pref[woman][match[woman]] > pref[woman][man]:
            P.add(match[woman])
            match[woman] = man
            match[man] = woman
        else:
            P.add(man)
    else: 
        match[woman] = man
        match[man] = woman

for i in range(n):
    print(p[i*2+1] + " -- " + p[match[i*2+1]])                    
