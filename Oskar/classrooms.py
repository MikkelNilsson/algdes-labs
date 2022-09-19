from queue import PriorityQueue

n, k = map(int, input().split())

activities = []
pq = PriorityQueue()

for i in range(n):
    (s, f) = map(int, input().split())
    activities.append((s, f))

activities.sort(key= lambda tup: tup[1])

for i in range(k):
    tmpAc = []
    

for (s, e) in activities:
    if (not pq.empty() and pq.queue[0][0] <= s):
        pq.put((e, pq.get()[1]+1))
    else:
        pq.put((e, 1))

l = sorted(pq.queue, key=lambda tup: tup[1], reverse=True)

counter = 0
for i in range(k):
    counter += l[i][1]

print(counter)





