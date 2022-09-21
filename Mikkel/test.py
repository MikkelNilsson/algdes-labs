from queue import PriorityQueue

pq = PriorityQueue()
pq.put(1)
pq.put(4)
pq.put(2)
pq.put(3)
print(pq.queue[0])
print(pq.get())
print(pq.queue)