import sys

def readall():
    v = input()
    try:
        while True:
            v += "\n" + input().strip()
    except EOFError:
        return v


def getarray():
    all = readall().split("\n")
    if ":" in all[0]:
        d = 1
        while all[d] != "NODE_COORD_SECTION":
            d += 1
        all = all[d+1:]
    while all[-1] == "EOF" or all[-1] == '':
        all = all[:-1]
    return all
            
    
input = getarray()
ctn = dict()
cl = list()
for v in input:
    vl = v.split(maxsplit=1)
    print(vl)
    n = vl[0]
    c = tuple(map(float, vl[1].split()))
    ctn[c] = n
    cl.append(c)

cl.sort(key=lambda x:x[0])
firstHalf, secondHalf = cl[:(len(cl)//2)],cl[(len(cl)//2):]
print("Below is the first half sorted:")
print(firstHalf)
print("")
print("Below is the second half sorted:")
print(secondHalf)
print("")




