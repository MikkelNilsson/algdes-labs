n = int(input())

for j in range(n):
    input()
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    
    
    xs.sort()
    ys.sort(reverse=True)
    
    sum = 0
    for i in range(len(xs)):
        sum += xs[i] * ys[i]
        
    print("Case #" + str(j + 1) + ": " + str(sum))