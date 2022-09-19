
n = int(input())

prices = list(map(int, input().split()))

prices.sort(reverse=True)
sum = 0
for i in range(2, n, 3):
    sum += prices[i]

print(sum)