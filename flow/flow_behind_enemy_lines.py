import parser

graph = parser.parseRails()
sink = len(graph)-1

def bfs(parent):

    visited = [False] * (sink + 1)

    queue = []

    queue.append(0)
    visited[0] = True

    while queue:
        v = queue.pop()

        for i, c in graph[v].items():
            if not visited[i] and c > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = v
                if i == sink:
                    return True
    
    return False

def run_ff_bfs():
    parent = [-1] * (sink + 1)
    maxflow = 0

    while bfs(parent):
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

print(flow)
