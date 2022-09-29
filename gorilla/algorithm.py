import parse_scheme
import Parser

def sequenceAlgo(m,n,x,y,gap,cost):
    M = [[None for _ in range(n+1)] for _ in range(m+1)]
    for i in range (0,m+1):
        M[i][0] = i * gap
    for j in range(0,n+1):
        M[0][j] = j * gap

    for i in range (1,m+1):
        for j in range (1,n+1):
            M[i][j] = max( cost[x[i-1]][y[j-1]] + M[i - 1][j - 1],
                gap + M[i- 1][j],
                gap + M[i][j - 1])
    return M[m][n]

input = Parser.inputProtein()
parsecost = parse_scheme.getcost()
for i, n in enumerate(input.keys()):
    for o in list(input.keys())[i+1:]:
        print(sequenceAlgo(len(input[n]), len(input[o]), input[n], input[o], -4, parsecost), n, o)
