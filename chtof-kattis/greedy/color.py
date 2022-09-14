s, c, k = map(int, input().split(" "))

inMachine = 0
machines = 1

socksList = list(map(int, input().split(" ")))
socksList.sort()

compareColor = socksList[0]

for sock in range(1, len(socksList)):
    if socksList[sock-1] == socksList[sock]:
        inMachine += 1
        if inMachine >= c:
            machines += 1
            inMachine = 0
            if sock != len(socksList)-1:
                compareColor = socksList[sock+1]
    if socksList[sock-1] < socksList[sock]:
        if socksList[sock] - socksList[sock-1] > k:
            machines += 1
            inMachine = 0
            compareColor = socksList[sock]
        else:
            inMachine += 1
            if inMachine >= c:
                machines += 1
                inMachine = 0
                if sock != len(socksList)-1:
                    compareColor = socksList[sock+1]
   

print(machines)   