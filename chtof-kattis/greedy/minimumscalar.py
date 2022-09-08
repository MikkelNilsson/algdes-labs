test = int(input())

for i in range(test):
    n = int(input())
    x = list(map(int,input().split(" ")))
    y = list(map(int,input().split(" ")))

    x.sort()
    y.sort(reverse=True)
    product = 0

    for j in range(n):
        product += x[j] * y[j]

    print("{}{}{}{}".format("Case #", i+1, ": ", product))
