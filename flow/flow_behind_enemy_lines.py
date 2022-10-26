from numpy import sort
import parser

graph = parser.parseRails()
sink = len(graph)-1

def bfs(parent):

    visited = [False] * (sink + 1)

    zero_edges = []

    queue = []

    queue.append(0)
    visited[0] = True

    while queue:
        v = queue.pop()

        for i, c in graph[v].items():
            if c > 0:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = v
                    if i == sink:
                        return (True, None, None)
            elif c == 0:
                zero_edges.append((v, i))
    
    return (False, zero_edges, visited)

def run_ff_bfs():
    parent = [-1] * (sink + 1)
    maxflow = 0

    while bfs(parent)[0]:
        pathflow = INF
        s = sink
        while s != 0:
            pathflow = min(pathflow, graph[parent[s]][s])
            s = parent[s]

        maxflow += pathflow
        
        v = sink
        while(v != 0):
            u = parent[v]
            graph[u][v] -= pathflow
            graph[v][u] += pathflow
            v = u

    return maxflow
 

INF = 10**6

flow = run_ff_bfs()


_, zero_edges, visited = bfs(([-1] * (sink + 1)))

res = []
for s, t in zero_edges:
    if not visited[t]:
        res.append((s, t, int(graph[t][s]/2)))

res = sorted(res, key=lambda x: x[0])

for s, t, c in res:
    print(s, t, c)