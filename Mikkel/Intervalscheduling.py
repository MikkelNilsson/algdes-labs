n = int(input())

l = list()

for _ in range(n):
    s, e = map(int, input().split())
    l.append((s, e))

l.sort(key=lambda x: x[1])

S = set()
t = 0
for e in l:
    if e[0] >= t:
        S.add(e)
        t = e[1]

print(len(S))
