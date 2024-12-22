f = open("input.txt")

lList = []
rList = []
for l in f:
    nr = l.split(" ")
    lList.append(int(nr[0]))
    rList.append(int(nr[-1]))
lList.sort()
rList.sort()

p1sum = 0
p2sum = 0
for i in range(len(lList)):
    p1sum += abs(lList[i] - rList[i])
    p2sum += lList[i] * rList.count(lList[i])
print("Part 1: "+str(p1sum))
print("Part 2: "+str(p2sum))

