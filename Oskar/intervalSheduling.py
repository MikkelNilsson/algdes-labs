
n = int(input())

intervals = []

for i in range(n):
    (s, f) = map(int, input().split())
    intervals.append((s, f))

intervals.sort(key= lambda tup: tup[1])

counter = 0
endtime = 0
for i in range(n):
    if (intervals[i][0] >= endtime):
       endtime = intervals[i][1]
       counter += 1

print(str(counter))



