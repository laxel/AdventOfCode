f = open("input.txt")

d = dict()
w = ['e','w','ne','nw','se','sw']
da = [1,-1,1,0,0,-1]
db = [0,0,1,1,-1,-1]
di = [1,1,2,2,2,2]

max_a, min_a = [0,0]
max_b, min_b = [0,0]

for l in f:
    if l[-1] == "\n":
        l = l[:-1]
    
    a,b = [0,0]
    i = 0
    
    while i < len(l):
        for j in range(len(w)):
            if l[i:i+di[j]] == w[j]:
                a += da[j]
                b += db[j]
                i += di[j]
    if not (a,b) in d:
        d[(a,b)] = True
    else:
        d[(a,b)] = not d[(a,b)]
    max_a = a if a > max_a else max_a
    min_a = a if a < min_a else min_a
    max_b = b if b > max_b else max_b
    min_b = b if b < min_b else min_b

# === Part 1 ===
res = 0
for k in d:
    if d[k]:
        res += 1
print("/P1/ Number of black tiles: " + str(res))

# === Part 2 ===
def num_neighbor(d,a,b):
    num_neigh = 0
    for i in range(6):
        if (a + da[i], b + db[i]) in d:
            num_neigh += 1 if d[(a + da[i], b + db[i])] else 0
    return num_neigh

for i in range(100):
    dw = d.copy()
    for a in range(min_a-2,max_a+2):
        for b in range(min_b-2,max_b+2):
            num_neig = num_neighbor(d,a,b)
            if (a,b) in d and d[(a,b)]:
                # Black tile
                if num_neig == 0 or num_neig > 2:
                    dw[(a,b)] = False
            else:
                #White tile
                if num_neig == 2:
                    dw[(a,b)] = True
                    max_a = a+1 if a >= max_a else max_a
                    min_a = a-1 if a <= min_a else min_a
                    max_b = b+1 if b >= max_b else max_b
                    min_b = b-1 if b <= min_b else min_b
    d = dw

res = 0
for k in d:
    if d[k]:
        res += 1
print("/P2/ Number of black tiles after 100 days: " + str(res))