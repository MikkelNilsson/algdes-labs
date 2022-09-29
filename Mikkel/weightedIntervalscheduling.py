import sys
sys.setrecursionlimit(10**6)

n = int(input())
tasks = list()

def binSearch(v, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2 

    if tasks[mid][1] <= v:
        if tasks[mid+1][1] <= v:
            return binSearch(v, mid + 1, high)
        else:
            return mid
    else:
        return binSearch(v, low, mid - 1)


        
[tasks.append(list(map(int, input().split()))) for _ in range(n)]
tasks.sort(key=lambda x: x[1])
p = [None] * n

for i, v in enumerate(tasks):
    p[i] = binSearch(v[0], 0, i-1)

cache = [None] * n

def maximizing(i):
    if cache[i]:
        return cache[i]
    if i == 0:
        return tasks[0][2]
    if p[i] == -1:
        return max(tasks[i][2], maximizing(i-1))
    cache[i] = max(maximizing(p[i]) + tasks[i][2], maximizing(i-1))
    return cache[i]

print(maximizing(n-1))