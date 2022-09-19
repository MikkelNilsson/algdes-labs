from cmath import sqrt
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
        (x1, y1) = list[0]
        (x2, y2) = list[1]
        return euclid(x1, y1, x2, y2)
    elif(len(list) < 2):
        return 100000000
    else:
        firstHalf, secondHalf = list[:(len(list)//2)],list[(len(list)//2):]
        bestLeft = int(rec(firstHalf))
        bestRight = int(rec(secondHalf))
        #Problem er complex tal, dem med E i 
        best = min(bestLeft, bestRight)
        return best

def euclid(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

def createYList(L1, L2, dist):
    newLeft  = []
    newRight = []


    len1 = len(L1)
    len2 = len(L2)
    mid = L1[len1-1][0] + (euclid((L1[len1-1][0]), 0, L2[0][0], 0))/2
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

firstHalf, secondHalf = cl[:(len(cl)//2)],cl[(len(cl)//2):]

(l, r) = createYList(firstHalf, secondHalf, 1000)
print(l)
print(r)






