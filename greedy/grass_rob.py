# [0] = n, 
    # [1] = l, 
    # [2] = w
count = []

while(True):
    try:
        countx = 0
        hihi = input()
        if(hihi == ''):
            break
        input_things = list(map(int, hihi.split(" ")))
        tup = list()
        for _ in range(input_things[0]):
            tup.append(tuple(map(int, input().split(" "))))

        # tup[0] = position
        # tup[1] = length

        tup.sort(key=lambda x : x[0])

        prev_val_behind = 0
        prev_val_forward = 0
        prev_pos = 0

        for (p, r) in tup:
            val_behind = p - r
            val_forward = p + r
            if val_behind < prev_val_forward: 
                prev_val_forward = val_forward 
                countx += 1
            if val_behind < prev_pos - 1:
                countx -= 1
            prev_pos = p


        # EDGE CASES START
        # THIS IS UGLY I KNOW DONT BOTHER TY
        islegit_wide = False
        for (p, r) in tup:
            val_behind = p - r
            val_forward = p + r
            if(val_forward) >= input_things[1]:
                islegit_wide = True

        islegit_height = True
        islegitlist = list()
        for (p, r) in tup:
            val_forward = 2 * r
            if(val_forward) >= input_things[2]:
                islegitlist.append(True)
            else:
                islegitlist.append(False)

        if all(x == False for x in islegitlist):
            islegit_height = False

        # EDGE CASES END

        if countx != 0 and islegit_wide and islegit_height:
            count.append(countx)
        else:
            count.append(-1)
    except:
        break

[print(x) for x in count]

