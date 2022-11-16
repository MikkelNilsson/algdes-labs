from queue import Queue
import math
from IndexMinPQ import IndexedMinPQ

n, m, r = map(int, input().split())
s, t = input().split()

adj = dict()
isRed = dict()
nameToIndex = dict()
indexToName = dict()

for i in range(n):
    tmpLine = input()
    if tmpLine.__contains__("*"):
        name, color = tmpLine.split()
        isRed[i] = True
        adj[i] = list()
        nameToIndex[name] = i
        indexToName[i] = name
    else:
        isRed[i] = False
        adj[i] = list()
        nameToIndex[tmpLine] = i
        indexToName[i] = tmpLine


for i in range(m):
    tmpLine = input()
    tmpList = tmpLine.split()
    u = tmpList[0]
    v = tmpList[-1]
    if tmpLine.__contains__(">"):
        adj[nameToIndex[u]].append(nameToIndex[v])
    else:
        adj[nameToIndex[u]].append(nameToIndex[v])
        adj[nameToIndex[v]].append(nameToIndex[u])
        

def bfs(start, toUseAdj):
    d = [math.inf]*n
    distance = 0
    queue = Queue(m)
    queue.put((start,0))
    d[start] = 0
    while not queue.empty():
        a = queue.get()
        distance = a[1]+1
        print(a[0])
        for elem in toUseAdj[a[0]]:
            if d[elem] == math.inf:
                queue.put((elem, distance))
                d[elem] = distance
    return d



def dijkstra(start, toUseAdj):
    edgeTo = [None]*n
    distTo = [math.inf]*n
    pq = IndexedMinPQ(n)
    distTo[start] = 0

    pq.insert(start, 0)
    while not pq.isEmpty():
        v = pq.deleteMin()
        for w, weight in toUseAdj[v]:
            if (distTo[w] > distTo[v] + weight):
                distTo[w] = distTo[v] + weight
                edgeTo[w] = v
                if (pq.contains(w)):
                    pq.decreaseKey(w, distTo[w])
                else:
                    pq.insert(w, distTo[w])
    
    return distTo


def few(start, terminal):
    tmpadj = adj.copy()
    for i in range(n):
        alternateList = []
        for a in tmpadj[i]:
            if isRed[a]:
                alternateList.append((a, 1))
            else:
                alternateList.append((a, 0))
        tmpadj[i] = alternateList
    
    dist = dijkstra(start, tmpadj)  
    print("Few")   
    print(tmpadj)
    print(dist)
    print()

    if isRed[start]:
        return dist[terminal]
    else:
        return dist[terminal]




def none(start, terminal):
    tmpadj = adj.copy()
    for a in tmpadj[start]:
        if a == terminal:
            return 1
    else:
        for i in range(n):
            if isRed[i]:
                tmpadj[i] = []
        
    dist = bfs(start, tmpadj)  
    print("None")   
    print(tmpadj)
    print(dist)
    print()

    return dist[terminal]


def alternate(start, terminal):   
    tmpadj = adj.copy() 
    for i in range(n):
        alternateList = []
        for a in tmpadj[i]:
            if isRed[i] != isRed[a]:
                alternateList.append(a)
        tmpadj[i] = alternateList
    
    result = bfs(start, tmpadj)

    print("Alternate")   
    print(tmpadj)
    print(result)
    print()

    if result[terminal] != math.inf:
        return True
    else: 
        return False


noneResult = none(nameToIndex[s], nameToIndex[t]) 
alternateResult = alternate(nameToIndex[s], nameToIndex[t]) 
fewResult = few(nameToIndex[s], nameToIndex[t]) 


print("Not Alternate")   
print(adj)
print()




print("result of none:", str(noneResult))
print("result of alternate:", str(alternateResult))
print("result of few:", str(fewResult))