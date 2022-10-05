import parse_scheme
import Parser

def sequenceAlgo(m,n,x,y,gap,cost):
    M = [[None for _ in range(n+1)] for _ in range(m+1)]
    for i in range (0,m+1):
        M[i][0] = (i * gap, x[:i], "-" * i)
    for j in range(0,n+1):
        M[0][j] = (j * gap, "-" * j, y[:j])

    for i in range (1,m+1):
        for j in range (1,n+1):
            v1 = cost[x[i-1]][y[j-1]] + M[i - 1][j - 1][0]
            v2 = gap + M[i- 1][j][0]
            v3 = gap + M[i][j - 1][0]
            if v1 >= v2 and v1 >= v3:
                t = M[i-1][j-1]
                M[i][j] = (v1, t[1] + x[i-1], t[2] + y[j-1])
            elif v2 >= v1 and v2 >= v3:
                t = M[i - 1][j]
                M[i][j] = (v2, t[1] + x[i-1], t[2] + "-")
            else: 
                t = M[i][j-1]
                M[i][j] = (v3, t[1] + "-", t[2] + y[j-1])

    return M[m][n]

input = Parser.inputProtein()
parsecost = parse_scheme.getcost()
for i, n in enumerate(input.keys()):
    for o in list(input.keys())[i+1:]:
        res = sequenceAlgo(len(input[n]), len(input[o]), input[n], input[o], -4, parsecost)
        print(n + "--" + o + ":", res[0])
        print(res[1])
        print(res[2])
