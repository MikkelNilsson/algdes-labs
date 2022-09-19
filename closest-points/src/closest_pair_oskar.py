def inputReader():
    i = input()
    if i.startswith("NAME:"):
        i = input()
        while (not i.startswith("NODE_COORD_SECTION")):
            i = input()
        return input()
    else:
        return i
