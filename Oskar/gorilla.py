for i in range(6):
    input()

letters = list(input().split())
scheme = dict()
for i in range(len(letters)):
    line = list(input().split())
    newDict = dict()
    for j in range(len(letters)):
        newDict[letters[j]] = line[j+1]
    scheme[line[0]] = newDict



print(scheme["P"]["Q"])