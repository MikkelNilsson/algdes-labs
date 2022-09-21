import math
from xmlrpc.client import MAXINT

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
    n = vl[0]
    c = tuple(map(float, vl[1].split()))
    ctn[c] = n
    cl.append(c)

def euclid(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
best = MAXINT
points = None
for i, p1 in enumerate(cl):
    for p2 in cl[:i]:
        dist = euclid(p1,p2)
        if dist < best:
            best = dist
            points = (p1, p2)

print(best, points)




