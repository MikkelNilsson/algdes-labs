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
        bestLeft = rec(firstHalf)
        bestRight = rec(secondHalf)
        best = min(bestLeft, bestRight)
        return best

def euclid(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
            
    
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





