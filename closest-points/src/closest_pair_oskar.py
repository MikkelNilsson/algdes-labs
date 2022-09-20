from math import sqrt
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

def rec(list):
    if(len(list) == 2):
        return euclid(list[0], list[1])
    elif(len(list) < 2):
        return -1
    else:
        firstHalf, secondHalf = list[:(len(list)//2)],list[(len(list)//2):]
        bestLeft = rec(firstHalf)
        bestRight = rec(secondHalf)
        if (bestLeft >= 0 and bestRight >= 0):
            best = min(bestLeft, bestRight)
        else:
            best = max(bestLeft, bestRight)
        (l, r) = createYList(firstHalf, secondHalf, best)
        l.sort(key=lambda x:x[1])
        r.sort(key=lambda x:x[1])

        #TODO Undersøg om alle muligheder bliver dækket
        for i in range(min(len(l), len(r))-1):
            e1 = euclid(l[i], r[i])
            e2 = euclid(l[i], r[i+1])
            e3 = euclid(l[i+1], r[i])
            best = min(best, e1, e2, e3)
        if(len(l) > 0 and len(r) > 0):
            best = min(best, euclid(l[len(l)-1], r[len(r)-1]))
            if(len(l) < len(r)):
                best = min(best, euclid(l[len(l)-1], r[len(r)-2]))
            elif(len(l) > len(r)):
                best = min(best, euclid(l[len(l)-2], r[len(r)-1]))

        return best

def euclid(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x2-x1)**2+(y2-y1)**2)

def createYList(L1, L2, dist):
    newLeft  = []
    newRight = []

    len1 = len(L1)
    len2 = len(L2)
    mid = L1[len1-1][0] + (euclid(((L1[len1-1][0]), 0), (L2[0][0], 0)))/2
    for i in range(len1):
        if (abs( mid - L1[len1-1-i][0]) > dist):
            continue
        else:
            newLeft.append(L1[len1-1-i])

    for i in range(len2):
        if (abs(L2[i][0] - mid) > dist):
            continue
        else:
            newLeft.append(L1[len1-1-i])

    return (newLeft, newRight)

            
    
input = getarray()
ctn = dict()
cl = list()
for v in input:
    vl = v.split(maxsplit=1)
    n = vl[0]
    c = tuple(map(float, vl[1].split()))
    ctn[c] = n
    cl.append(c)

cl.sort(key=lambda x:x[0])

print(str(rec(cl)))






