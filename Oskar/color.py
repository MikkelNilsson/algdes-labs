import math

s, c, k = map(int, input().split())


socks = list(map(int, input().split()))

socks.sort()
maxMachines = math.ceil(s/c)

machineCounter = 1
compareColor = socks[0]
socksInMachine = 0
for i in range(s):
    if (socks[i] - compareColor <= k ):
        socksInMachine += 1
        if (socksInMachine == c):
            socksInMachine = 0
            if (i != s-1):
                compareColor = socks[i+1]
                machineCounter += 1
    else:
        socksInMachine = 1
        if (not i == s-1):
            compareColor = socks[i]
        machineCounter += 1

        
print(machineCounter)