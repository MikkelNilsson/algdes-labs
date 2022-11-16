from queue import Queue
import math

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
        

def bfs(start):
    d = [math.inf]*n
    distance = 0
    queue = Queue(m)
    queue.put((start,0))
    d[start] = 0
    while not queue.empty():
        a = queue.get()
        distance = a[1]+1
        print(a[0])
        for elem in adj[a[0]]:
            if d[elem] == math.inf:
                queue.put((elem, distance))
                d[elem] = distance
    return d


def none(start, terminal):
    for a in adj[start]:
        if a == terminal:
            return 1
    else:
        for i in range(n):
            if isRed[i]:
                adj[i] = []
        
    dist = bfs(start)  
    print("None")   
    print(adj)
    print(dist)
    print()

    return dist[terminal]


def alternate(start, terminal):
    print("Before alternate")   
    print(adj)
    print()
    
    for i in range(n):
        alternateList = []
        for a in adj[i]:
            if isRed[i] != isRed[a]:
                alternateList.append(a)
        adj[i] = alternateList
    
    result = bfs(start)

    print("Alternate")   
    print(adj)
    print(result)
    print()

    if result[terminal] != math.inf:
        return True
    else: 
        return False


distt = alternate(nameToIndex[s], nameToIndex[t]) 





print("result", str(distt))