from ast import Return
import math

n = int(input())
for i in range(n):
    cache = dict()
    coins = []
    toPay = int(input())
    numberCoins = int(input())
    for j in range(numberCoins):
        coin = int(input())
        coins.append(coin)
        cache[coin] = 1

    def min_coins(p, coinIndex):
        if p == 0:
            return 0
        if p < 0 or coinIndex < 0:
            return math.inf
        if (p, coinIndex) in cache:
            return cache[(p, coinIndex)]
        else:
            result = min(min_coins(p-coins[coinIndex], coinIndex-1)+1, min_coins(p, coinIndex-1))
            cache[(p, coinIndex)] = result
            return result


    
    for x in range(toPay, 20000):
        coinsUsed = min_coins(x, numberCoins-1)
        if coinsUsed < math.inf:
            print(x, coinsUsed)
            break
