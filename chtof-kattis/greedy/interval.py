n = int(input())

intervals = list()

for _ in range(n):
    intervals.append(list(map(int, input().split(" "))))

intervals.sort(key=lambda x:x[1])

count = 0
flast = 0

for (s,f) in intervals:
    if s >= flast:
        flast = f
        count +=1

print (count)
