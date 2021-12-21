import re

f = open("input.txt")

td = dict()
cm = ""
tc = []
for l in f:
    if m := re.match("Tile (\\d+)",l):
        if cm != "":
            td[cm] = tc
            tc = []
        cm = m.group(1)
    elif l != "\n":
        tc.append([c for c in l if c != '\n'])
td[cm] = tc

#for k in d:
#    tc = d[k]
#    print("Tile: " + k)
#    for r in tc:
#        print(r)
#    print("")

def add_d(d,v):
    if not v in d:
        d[v] = 1
    else:
        d[v] += 1

def cntd_add_d(d,k,v):
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]

num_d = dict()
nt_d = dict()
cntd_d = dict()

for k in td:
    tc = td[k]
    nt_d[k] = []
    # Top
    b = "".join(list(map(lambda x: '0' if x == '.' else '1' , tc[0])))
    add_d(num_d,int(b,2))
    add_d(num_d,int(b[::-1], 2))
    nt_d[k].append([int(b,2),int(b[::-1], 2)])
    cntd_add_d(cntd_d,int(b,2),k)
    cntd_add_d(cntd_d,int(b[::-1],2),k)

    # Right
    b = ''
    for r in tc:
        b += '0' if r[-1] == '.' else '1'
    add_d(num_d,int(b,2))
    add_d(num_d,int(b[::-1], 2))
    nt_d[k].append([int(b,2),int(b[::-1], 2)])
    cntd_add_d(cntd_d,int(b,2),k)
    cntd_add_d(cntd_d,int(b[::-1],2),k)

    # Bottom
    b = "".join(list(map(lambda x: '0' if x == '.' else '1' , tc[-1])))
    add_d(num_d,int(b,2))
    add_d(num_d,int(b[::-1], 2))
    nt_d[k].append([int(b,2),int(b[::-1], 2)])
    cntd_add_d(cntd_d,int(b,2),k)
    cntd_add_d(cntd_d,int(b[::-1],2),k)

    # Left
    b = ''
    for r in tc:
        b += '0' if r[0] == '.' else '1'
    add_d(num_d,int(b,2))
    add_d(num_d,int(b[::-1], 2))
    nt_d[k].append([int(b,2),int(b[::-1], 2)])
    cntd_add_d(cntd_d,int(b,2),k)
    cntd_add_d(cntd_d,int(b[::-1],2),k)

    
#for k in num_d:
#    print(str(k) + ": " + str(num_d[k]))

prod = 1
corner = ""
for nt_k in nt_d:
    c = nt_d[nt_k]
    empty_sides = 0
    for l in c:
        if num_d[l[0]] == 1:
            empty_sides += 1
    if empty_sides == 2:
        print("Corner: " + nt_k)
        corner = nt_k
        prod *= int(nt_k)

print("/P1/ Product of the corner IDs: " + str(prod))

print(nt_d)
print("")
print(nt_d['1951'])
print([num_d[x[0]] for x in nt_d['1951']])
print("")
print(cntd_d)
print("")

map_d = dict()

done = []
todo = [corner]
todo_c = [[0,0]]
while len(todo) > 0:
    # Get new Tile to check
    current = todo.pop()
    x, y = todo_c.pop()
    # Get list of connected sides
    s_values = nt_d[current]
    # Loop throught each side, find connected tiles, and add them to todo
    for i in range(len(s_values)):
        s_v = s_values[i][0]
        # Check if side is not on edge/corner
        if num_d[s_v] == 2:
            l = cntd_d[s_v]
            l.remove(current)
            print(l)
            print(i)
            