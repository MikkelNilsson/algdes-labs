
import math


def parseRails():
    nrnodes = int(input())
    arcs = dict([(i, dict()) for i in range(nrnodes)])

    for _ in range(nrnodes):
        input()

    nrarcs = int(input())
    for _ in range(nrarcs):
        u, v, c = map(int, input().split(" "))
        if c == -1: 
            c = math.inf
        arcs[u][v] = c
        arcs[v][u] = c

    return arcs
    