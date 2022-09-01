def inputthings(): 
    i = input()
    if i.startswith("#"):
        inputthings()
    return i

n = int(inputthings().split("=")[1])

people = dict()

for _ in range(2*n):
    y = input().split()
    people[y[0]] = y[1]
    
input()

proposers = list()
non_proposers = list()

for x in range(2*n):
    y = input().split(": ")
    temp_dict = dict()
    temp_dict[y[0]] = list(map(int,(y[1]).split(" "))) # e.g. [1: 2,4]
    if x % 2 == 0:
        proposers.append(temp_dict)
    else:
        non_proposers.append(temp_dict)

print(proposers)
# proposers [[1: 2,4], [2: 3,1]]
# non_proposers [[3: 4,2], [4: 1,3]]
# for x in proposers:
#     while()