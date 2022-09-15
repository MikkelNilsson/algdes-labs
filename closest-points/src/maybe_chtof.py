


#[(name,x,y),(name1,x1,y1),(name2,x2,y2)]
name = []
coords = []
try:
    while True:
        i = input()
        print(i)
        name.append(i.split(" ")[0])
        coords.append(list(map(float, i.split(" ")[1:])))
        if i == "":
            break
except EOFError:
    pass        

toBeSorted = list(zip(name,coords))

print("list before it is sorted:")
print(toBeSorted)
print("")
toBeSorted.sort(key=lambda x:x[1])
print("List after sorting:")
print(toBeSorted)
print("")

firstHalf, secondHalf = toBeSorted[:(len(toBeSorted)//2)],toBeSorted[(len(toBeSorted)//2):]

print("Below is the first half sorted:")
print(firstHalf)
print("")
print("Below is the second half sorted:")
print(secondHalf)
print("")
