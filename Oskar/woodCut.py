
t = int(input())

for i in range(t):
    wait = 0
    n = int(input())
    costomers = []
    for j in range(n):
        sum = 0
        pieces = list(map(int, input().split()))
        for k in range(1, len(pieces)):
            sum += pieces[k]
        costomers.append(sum)
    costomers.sort()
    for j in range(1, n):
        costomers[j] += costomers[j-1]
    
    for j in range(n):
        wait += costomers[j]
    avg = wait/n
    print(avg)