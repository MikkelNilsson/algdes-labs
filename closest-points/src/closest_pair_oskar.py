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
        return (euclid(list[0], list[1]), (list[0], list[1]))
    elif(len(list) < 2):
        return (-1, (-1,-1))
    else:
        firstHalf, secondHalf = list[:(len(list)//2)],list[(len(list)//2):]
        (bestLeft, pointsLeft) = rec(firstHalf)
        
        (bestRight, pointsRight) = rec(secondHalf)

        if (bestLeft >= 0 and bestRight >= 0):
            if (bestLeft < bestRight):
                best = bestLeft
                bestPoints = pointsLeft
            else:
                best = bestRight
                bestPoints = pointsRight
        else:
            if (bestLeft > bestRight):
                best = bestLeft
                bestPoints = pointsLeft
            else:
                best = bestRight
                bestPoints = pointsRight

        yList = createYList(firstHalf, secondHalf, best)
        yList.sort(key=lambda x:x[1])
        
        size = len(yList)
        for i in range(size):
            j = i + 1
            while j < size and (yList[j][1] - yList[i][1]) < best:
                newBest = euclid(yList[j], yList[i])
                if (newBest < best):
                    best = newBest
                    bestPoints = (yList[i], yList[j])
                j += 1
    
        return (best, bestPoints)

def euclid(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x2-x1)**2+(y2-y1)**2)

def createYList(L1, L2, dist):
    newList  = []
    
    len1 = len(L1)
    len2 = len(L2)
    mid = (L1[len1-1][0] + L2[0][0])/2
    for i in range(len1):
        if (abs( mid - L1[len1-1-i][0]) > dist):
            continue
        else:
            newList.append(L1[len1-1-i])

    for i in range(len2):
        if (abs(L2[i][0] - mid) > dist):
            continue
        else:
            newList.append(L2[i])

    return newList


            
    
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

result, resultPoints = rec(cl)
(x1, y1) = resultPoints[0]
(x2, y2) = resultPoints[1]

print(str(result))
print(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))






