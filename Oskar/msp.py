
t = int(input())


for i in range(1, t+1):
    n = int(input())
    vector1 = list(map(int, input().split()))
    vector2 = list(map(int, input().split()))
    vector1.sort()
    vector2.sort(reverse=True)

    acc = 0
    for j in range(n):
        acc += vector1[j]*vector2[j]

    print("Case #" + str(i) + ": " + str(acc))


