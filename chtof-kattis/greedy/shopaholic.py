n = int(input())

rabat = 0

priser = list(map(int, input().split()))
priser.sort(reverse=True)

for i in range(2, n, 3):
    rabat += priser[i]

print(rabat)
