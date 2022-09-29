
def inputProtein():
    s = input().split()[0].strip(">")
    proteinstrings = dict()
    p = ""
    inp = input()
    try:
        while True:
            if ">" not in inp:
                p += inp
                inp = input()
            else:
                proteinstrings[s] = p
                p = ""
                s = inp.split()[0].strip(">")
                inp = input()

    except EOFError:
        proteinstrings[s] = p
        return proteinstrings



