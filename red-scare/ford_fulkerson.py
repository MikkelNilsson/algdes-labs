
INF = 10**6

def bfs(adj_dict, n, source, sink, parent):

    visited = [False] * n

    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        v = queue.pop()
        for i, c in adj_dict[v].items():
            if c > 0:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = v
                    if i == sink:
                        return True

    
    return False

def run_ff_bfs(adj_dict, n, source, sink):
    parent = [-1] * n
    maxflow = 0

    while bfs(adj_dict, n, source, sink, parent):
        pathflow = INF
        s = sink
        while s != source:
            pathflow = min(pathflow, adj_dict[parent[s]][s])
            s = parent[s]

        maxflow += pathflow
        
        v = sink
        while(v != source):
            u = parent[v]
            adj_dict[u][v] -= pathflow
            adj_dict[v][u] += pathflow
            v = u

    return maxflow