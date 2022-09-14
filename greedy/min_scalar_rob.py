n = int(input())
n_left = n
c = 1
while n_left > 0:
    result = 0
    collumns = int(input())
    x_list = list(map(int, input().split(" ")))
    y_list = list(map(int, input().split(" ")))
    x_list.sort()
    y_list.sort(reverse=True)
    for i in range(collumns):
        result += x_list[i] * y_list[i]
    print(f'Case #{c}: {result}')
    c += 1
    n_left -= 1
    