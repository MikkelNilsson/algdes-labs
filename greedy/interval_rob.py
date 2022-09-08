input_rows = int(input())

intervals = []

for _ in range(input_rows):
    intervals.append(tuple(map(int, input().split(" ")))) # nasty oneliner ew

intervals.sort(key=lambda x : x[1]) # sorted by end time. This is python hackz

prev_end = -1
count = 0

for (s, e) in intervals:
    if s >= prev_end: # if new start time is greater than prev_end
        prev_end = e # updating
        count += 1 # incrementing number of intervals in the schedule

print(count)