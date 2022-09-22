n = int(input())

interval = []

for _ in range (n):
    ## Gives list of tuples (start, finish, weight)
    interval.append(list(map(int, input().split(" "))))

interval.sort(key=lambda x:x[1])

m = [None] * n-1


def binarySearch(j, start):
 
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start- 1
 
    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if j[mid][1] <= j[start][0]:
            if j[mid + 1][1] <= j[start][0]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

# The main function that returns the maximum possible
# profit from given list of js
def schedule(j):
   
    m[0] = j[0][2]
 
    # Fill entries in table[] using recursive property
    for i in range(1, n):
 
        # Find profit including the current job
        inclProf = j[i][2]
        l = binarySearch(j, i)
        if (l != -1):
            inclProf += m[l]
 
        # Store maximum of including and excluding
        m[i] = max(inclProf, m[i - 1])
 
    return m[n-1]  


print(schedule(interval))


