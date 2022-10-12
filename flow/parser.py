def parseRails():
    nrnodes = int(input())
    nodes = list()
    arcs = list()
    for _ in range(nrnodes):
        node = input()
        nodes.append(node[:-1])
    print("Here comes the nodes \n")
    print(nodes)
    nrarcs = int(input())
    for _ in range(nrarcs):
        u, v, c = map(int, input().split(" "))
        arcs.append((u,v,c))
    print("\nHere comes the arcs \n")
    print(arcs)    

parseRails()