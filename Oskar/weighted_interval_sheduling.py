import sys

sys.setrecursionlimit(10**6)
def binarySearch(value, lo, hi):
    
    while lo <= hi:
        mid = (hi + lo) // 2
        if intervals[mid][1] <= value:
            if intervals[mid + 1][1] <= value:
                lo = mid+1
            else:
                return mid
        else:
            hi = mid-1
    return -1

def opt(j):
    if cache[j] != None:
        return cache[j]
    if j == 0:
        return intervals[0][2]
    if P[j] < 0:
        return max(intervals[j][2], opt(j-1))
    
    take = intervals[j][2] + opt(P[j])
    drop = opt(j-1)
    cache[j] = max(take, drop)

    return cache[j]


n = int(input())

intervals = []

for _ in range(n):
    intervals.append(list(map(int, input().split())))

intervals.sort(key=lambda x:x[1])
cache = [None] * n

P = [None] * n
P[0] = 0
for i, interval in enumerate(intervals):
    P[i] = binarySearch(interval[0], 0, i-1)
    
print(opt(n-1))


