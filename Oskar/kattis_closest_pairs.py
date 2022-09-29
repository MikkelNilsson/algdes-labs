from math import sqrt
import sys

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
        yList.sort(key=lambda x:x[1]) # O(N log N)
        
        size = len(yList)
        for i in range(size): # O(N)
            j = i + 1
            while j-i < 15 and j < size and (yList[j][1] - yList[i][1]) < best: # for the explanaition of the constant 15 look at statement 5.10 in the book.
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
    mid = L1[len1-1][0] + (euclid(((L1[len1-1][0]), 0), (L2[0][0], 0)))/2
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


while(True):
    n = int(input())
    if (n==0):
        break
    points = []
    for i in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    points.sort(key=lambda x:x[0])
    resultPoints = rec(points)[1]
    (x1, y1) = resultPoints[0]
    (x2, y2) = resultPoints[1]
    print(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))