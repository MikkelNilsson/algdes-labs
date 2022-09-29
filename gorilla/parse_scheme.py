f = open(".\data\BLOSUM62.txt", "r")

for i in range(6):
    f.readline()

letters = list(f.readline().split())
scheme = dict()
for i in range(len(letters)):
    line = list(f.readline().split())
    newDict = dict()
    for j in range(len(letters)):
        newDict[letters[j]] = line[j+1]
    scheme[line[0]] = newDict



print(scheme)