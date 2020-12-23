# === Parsing ===
rl = open("input.txt").readlines()

hi = rl.index("Player 2:\n")

_p1 = [int(x) for x in rl[1:hi-1]]
_p2 = [int(x) for x in rl[hi+1:]]
p1 = _p1.copy()
p2 = _p2.copy()

# === Part 1 ===
while not len(p1) > 0 and len(p2) > 0:
    v1 = p1.pop(0)
    v2 = p2.pop(0)
    if v1 > v2:
        p1.append(v1)
        p1.append(v2)
    else:
        p2.append(v2)
        p2.append(v1)

wl = p1 if len(p1) != 0 else p2
res = 0
for i in range(len(wl)):
    res += wl[i] * (len(wl) - i)
print("/P1/ sum of deck: " + str(res))

# === Part 2 ===
def rec_combat(p1,p2):
    prev_combs = set()
    while len(p1) > 0 and len(p2) > 0:
        word = ''.join([str(x)+',' for x in p1]) + ':' \
            +  ''.join([str(x)+',' for x in p2])
        if word in prev_combs:
            return [1,p1]
        else:
            prev_combs.add(word)
        
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        
        wnr = 0
        if v1 <= len(p1) and v2 <= len(p2):
            wnr = rec_combat(p1.copy()[0:v1], p2.copy()[0:v2])[0]
        else:
            wnr = 1 if v1 > v2 else 2

        if wnr == 1:
            p1.append(v1)
            p1.append(v2)
        else:
            p2.append(v2)
            p2.append(v1)
        

    return [1,p1] if len(p1) != 0 else [2,p2]

p1 = _p1.copy()
p2 = _p2.copy()
print("Might take a couple of seconds...")
w, wl = rec_combat(p1,p2)
res = 0
for i in range(len(wl)):
    res += wl[i] * (len(wl) - i)
print("/P2/ sum of deck: " + str(res))

