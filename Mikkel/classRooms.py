from queue import PriorityQueue

n, r = map(int, input().split())

rl = list()

for _ in range(n):
    s, e = map(int, input().split())
    rl.append((s, e))

rl.sort(key=lambda x: x[0])

pq = PriorityQueue()

for (s, e) in rl:
    if not pq.empty() and pq.queue[0][0] <= s:
        (_, i) = pq.get()
        pq.put((e, i+1))
    elif len(pq.queue) < r:
        pq.put((e, 1))


sum = 0
for (_, l) in pq.queue:
    sum += l
print(str(sum))

#l = sorted(pq.queue, key=lambda x: x[1], reverse=True)





#sum = 0
#for i in range(r):
#    sum += l[i][1]
#print(str(sum))


#print(l)
#print(str(l[0][1] + l[1][1]))

