import os
from random import SystemRandom

with open("closest-pair-out.txt", "r") as f:
    l = f.readline()
    while l != "#":
        filename = l.split(": ")[0].replace(".t", "-t")
        #print (filename)
        res = l.split(": ")[1].split(" ")[1]
        sysres = os.system("python ../src/closest_pair_oskar.py < " + filename + ".txt")
        
        if res != sysres.split("\n")[0]:
            print ("Error on:", filename, "\n", res, sysres.split("\n")[0], "\n\n")
        l = f.readline()

    