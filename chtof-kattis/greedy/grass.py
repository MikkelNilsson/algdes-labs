ins = list(map(float,input().split(" ")))

sprinklers = int(ins[0])
length = ins[1]
width = ins[2]

print(ins)

tups = list()
for i in range (sprinklers):
    tups.append(list(map(float,input().split(" "))))

tups.sort(key=lambda x:x[0])    

newtups = list()

for (p,r) in tups:
    if r*2 <= width:
        continue
    else:
        newtups.append((p,r-0.5))


waterBackward = 0.0
waterForward = 0.0
count = 0
prevpos = 0.0

for (p,r) in newtups:
    tupBackward = p-r
    tupForward = p+r
    if tupBackward <= waterForward: 
        waterForward = tupForward
        count += 1
    if tupBackward < prevpos -0.5:
        count -= 1        
    prevpos = p    

print(count)        
