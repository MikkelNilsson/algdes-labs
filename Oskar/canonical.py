import math

n = int(input())

coins = list(map(int, input().split()))
largestAmount = coins[-1] + coins[-1]
cache = [math.inf] * (largestAmount)

cache[0] = 0
cache[1] = 1

#coins.sort(reverse=True)
def greedy(amount):
    counter = 0
    missingAmount = amount
    coinIndex = len(coins)-1
    while (missingAmount > 0):
        tmp = missingAmount // coins[coinIndex]
        counter += tmp
        missingAmount = missingAmount % coins[coinIndex]
        coinIndex -= 1 
    return counter

    
canonical = True

for i in range(2, largestAmount):
    for coin in coins:
        missing = i - coin
        if (missing >= 0):
            cache[i] = min(cache[missing] + 1, cache[i])
        else:
            break

    if (greedy(i) != cache[i]):
        canonical = False
        break


if(canonical): 
    print("canonical")
else:
    print("non-canonical")

