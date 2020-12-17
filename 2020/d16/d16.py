import re
import itertools

f = open("input.txt")

# === Part 1 ===
valid_l = []
ts = []
my_ticket = []
stage = 0
num_para = 0
for l in f:
    if l == "your ticket:\n" or l == "nearby tickets:\n":
        stage += 1
    if stage == 0:
        m = re.search("(\d+)-(\d+) or (\d+)-(\d+)",l)
        if m:
            valid_p = []
            valid_p.append([int(m.group(1)), int(m.group(2))])
            valid_p.append([int(m.group(3)), int(m.group(4))])
            valid_l.append(valid_p)
    if stage == 1:
        m = re.findall("(\d+)",l)
        if len(m) != 0: 
            num_para = len(m)
            [my_ticket.append(int(x)) for x in m]
    if stage == 2:
        m = re.findall("(\d+)",l)
        if len(m) != 0: 
            t = []
            [t.append(int(x)) for x in m]
            ts.append(t)


c_invalid = []
bad_tickets = []
for i in range(len(ts)):
    for n in ts[i]:
        is_kinda_Valid = False
        for l in valid_l:
            for p in l:
                if p[0] <= n <= p[1]:
                    is_kinda_Valid = True
        if not is_kinda_Valid:
            c_invalid.append(n)
            bad_tickets.append(i)
    
print("/P1/ Sum of completly invalid: " + str(sum(c_invalid)))

# === Part 2 ===
v_ts = [] # Valid tickets
for i in range(len(ts)):
    if i not in bad_tickets:
        v_ts.append(ts[i])

# Check for whole colum what fields are possible
c_possible = []
for c in range(num_para):
    possible_fields = []
    for j in range(len(valid_l)):
        is_possiple = True
        f = valid_l[j]
        a = f[0]
        b = f[1]
        for t in v_ts:
            c_v = t[c]
            if not (a[0] <= c_v <= a[1] or b[0] <= c_v <= b[1]):
                is_possiple = False
                break
        if is_possiple:
            possible_fields.append(j)
    c_possible.append(possible_fields)

i = 0
done = []
while True:
    l = c_possible[i]
    if len(l) == 1 and i not in done:
        v = l[0]
        for j in range(len(c_possible)):
            if i == j:
                continue
            if v in c_possible[j]:
                c_possible[j].remove(v)
        done.append(i)
        i = -1
    i += 1
    if i >= len(c_possible):
        break

p2_res = 1
for i in range(len(c_possible)):
    j = c_possible[i][0]
    if j < 6:
        p2_res *= my_ticket[i]

print("/P2/ Sum of departure values: " + str(p2_res))
        