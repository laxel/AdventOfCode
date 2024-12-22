f = open("input.txt")

# Parse imput
rdict = {}
updates = []
phase = 0
for l in f:
    if l == '\n':
        phase = 1
        continue
    if phase == 0:
        a,b = l.split("|")
        if int(a) not in rdict:
            rdict[int(a)] = [int(b)]
        else:
            rdict[int(a)] += [int(b)]
    else:
        updates.append([int(x) for x in l.split(",")])

p1_sum = 0
iupdates = []
for u in updates:
    valid = True
    for i in range(len(u)):
        if u[i] in rdict:
            for j in range(0,i):
                if u[j] in rdict[u[i]]:
                    valid = False
    if valid:
        p1_sum += u[int(len(u)/2)]
    else:
        iupdates.append(u)
print("Part 1: "+str(p1_sum))

p2_sum = 0
for u in iupdates:
    for i in range(len(u)):
        if u[i] in rdict:
            for j in range(0,i):
                if u[i] in rdict and u[j] in rdict[u[i]]:
                    u.insert(j,u[i])
                    del u[i+1]
    p2_sum += u[int(len(u)/2)]
print("Part 2: "+str(p2_sum))
