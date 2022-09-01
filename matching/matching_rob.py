def inputthings(): 
    i = input()
    if i.startswith("#"):
        return inputthings()
    return i

n = int(inputthings().split("=")[1])

people = dict()

for _ in range(2*n):
    y = input().split()
    people[y[0]] = y[1]
    
input()

proposers = dict()
non_proposers = dict()

for x in range(2*n):
    ratingdict = dict()
    y = input().split(": ")
    int_id = int(y[0])
    temp_dict = dict()
    int_pref = list(map(int,y[1].split(" "))) # e.g. [1: 2,4]
    if int(y[0]) % 2 == 0:
        for counter, i in enumerate(int_pref):
            ratingdict[i] = counter            
        non_proposers[y[0]] = ratingdict
    else:
        proposers[y[0]] = int_pref

def GetOddNumbers(n):
    temp = list()
    for x in range(n):
        temp.append(x*2+1)
    return temp

proposer_indexes = GetOddNumbers(n)

print(proposer_indexes)
print(proposers)
print(non_proposers)
# proposers {'1': [2, 4], '3': [4, 2]}
# non_proposers {'2': {3: 0, 1: 1}, '4': {1: 0, 3: 1}}
