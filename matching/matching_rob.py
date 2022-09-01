from collections import defaultdict


def inputthings(): 
    i = input()
    if i.startswith("#"):
        return inputthings()
    return i

def GetOddNumbersAsSet(n):
    temp = set()
    for x in range(n):
        temp.add(x*2+1)
    return temp

n = int(inputthings().split("=")[1])

people = dict()

for _ in range(2*n):
    y = input().split()
    people[int(y[0])] = y[1]
    
input()

kms = dict()

for x in range(2*n):
    ratingdict = dict()
    y = input().split(": ")
    int_id = int(y[0])
    temp_dict = dict()
    int_pref = list(map(int,y[1].split(" "))) # e.g. [1: 2,4]
    if int_id % 2 == 0:
        for counter, i in enumerate(int_pref):
            ratingdict[i] = counter            
        kms[int_id] = ratingdict
    else:
        kms[int_id] = int_pref


proposer_ids = GetOddNumbersAsSet(n)

matches = defaultdict(lambda : None)

print(kms)

while(len(proposer_ids) > 0):
    curr_proposer = proposer_ids.pop()
    curr_non_proposer = kms[curr_proposer].pop(0)
    if matches[curr_non_proposer]:
        if kms[curr_non_proposer][matches[curr_non_proposer]] > kms[curr_non_proposer][curr_proposer]:
            #comparing current matched proposers rating with asking proposers rating
            proposer_ids.add(matches[curr_non_proposer])
            matches[curr_non_proposer] = curr_proposer
        else:
            proposer_ids.add(curr_proposer)
    else:
        matches[curr_proposer] = curr_non_proposer

for i in range(n):
    print(people[i*2+1], " + ", people[matches[i*2+1]])
    

