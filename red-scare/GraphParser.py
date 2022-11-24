from queue import Queue
import math
from IndexMinPQ import IndexedMinPQ
import ford_fulkerson
from os import listdir

def run(fileName):
    with open("data\\" + fileName) as f:
        n, m, r = map(int, f.readline().split())
        s, t = f.readline().split()

        adj = dict()
        isRed = dict()
        red = set()
        nameToIndex = dict()
        indexToName = dict()
        directed = False

        for i in range(n):
            tmpLine = f.readline().strip()
            if tmpLine.__contains__("*"):
                name, color = tmpLine.split()
                isRed[i] = True
                red.add(i)
                adj[i] = list()
                nameToIndex[name] = i
                indexToName[i] = name
            else:
                isRed[i] = False
                adj[i] = list()
                nameToIndex[tmpLine] = i
                indexToName[i] = tmpLine

        
        for i in range(m):
            tmpLine = f.readline()
            tmpList = tmpLine.split()
            u = tmpList[0]
            v = tmpList[-1]
            if tmpLine.__contains__(">"):
                adj[nameToIndex[u]].append(nameToIndex[v])
                directed = True
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
                for elem in toUseAdj[a[0]]:
                    if d[elem] == math.inf:
                        queue.put((elem, distance))
                        d[elem] = distance
            return d


        def isDAG(start):
            d = [math.inf]*n
            marked = [False]*n
            distance = 0
            queue = Queue(m)
            queue.put((start,0))
            d[start] = 0
            marked[start] = True
            while not queue.empty():
                a = queue.get()
                marked[a[0]] = True
                distance = a[1]+1
                for elem in adj[a[0]]:
                    if marked[elem]:
                        return False

                    if d[elem] == math.inf:
                        queue.put((elem, distance))
                        d[elem] = distance
            return True


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
            
            if dist[terminal] == math.inf:
                return -1
            elif isRed[start]:
                return dist[terminal]
            else:
                return dist[terminal]


        def findMany(start, terminal, toUseAdj, mem):
            max = - math.inf
            if start == terminal:
                return 0
            elif mem[start] != math.inf:
                return mem[start]
            else:
                for a, weight in toUseAdj[start]:
                    tmp = weight + findMany(a, terminal, toUseAdj, mem)
                    if tmp > max:
                        max = tmp   

                mem[start] = max
                return max


        def many(start, terminal):
            if isDAG(start):
                tmpadj = adj.copy()
                for i in range(n):
                    alternateList = []
                    for a in tmpadj[i]:
                        if isRed[a]:
                            alternateList.append((a, 1))
                        else:
                            alternateList.append((a, 0))
                    tmpadj[i] = alternateList

                memory = [math.inf]*n

                dist = findMany(start, terminal, tmpadj, memory)
                if dist == -math.inf:
                    return -1
                elif isRed[start]:
                    return dist + 1
                else:
                    return dist
            
            else: 
                print("The graph in question was not a DAG, and many can therefore not be solved")
                return -1

            

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

            if dist[terminal] == math.inf:
                return -1
            else:
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

            if result[terminal] != math.inf:
                return True
            else: 
                return False

        def some(start, terminal):
            if directed:
                print("Graph is directed, and Some can therefore not be solved.")
                return False
            
            some_adj = adj.copy()
            for i in range(n):
                alternateList = []
                for a in some_adj[i]:
                    alternateList.append((a, 1))
                some_adj[i] = dict(alternateList)

            some_adj[n] = {start: 1, terminal: 1}
            some_adj[start][n] = 1
            some_adj[terminal][n] = 1
                
            for vr in red:
                if ford_fulkerson.run_ff_bfs(some_adj, n + 1, n, vr) == 2:
                    return True
            
            return False
                



        noneResult = none(nameToIndex[s], nameToIndex[t]) 
        print("result of none:", str(noneResult))
        alternateResult = alternate(nameToIndex[s], nameToIndex[t]) 
        print("result of alternate:", str(alternateResult))
        fewResult = few(nameToIndex[s], nameToIndex[t])
        print("result of few:", str(fewResult))
        manyResult = many(nameToIndex[s], nameToIndex[t])
        print("result of many:", str(manyResult))
        someResult = some(nameToIndex[s], nameToIndex[t])
        print("result of Some:", someResult)
        print()

        if fewResult > 0 and not someResult:
            print("\nERRROROROROORORORO\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            

        """print("Not Alternate")   
        print(adj)
        print()"""



inputList = listdir("data")

for inp in inputList:
    if inp != "README.md":
        print(inp)
        run(inp)