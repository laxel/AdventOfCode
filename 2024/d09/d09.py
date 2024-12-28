import copy
f = open("input.txt")
line = f.readline()

ftype = True
mem   = []
id    = 0
p2_type = []
for c in line:
    if c == '\n': continue
    if ftype:
        mem += [id]*int(c)
        p2_type += [[id, int(c), False]]
        id += 1
    else:
        mem += [-1]*int(c)
        p2_type += [[-1, int(c), True]]

    ftype = not ftype
# Calculate list of reverse file id order
rmem = [x for x in list(reversed(mem)) if x != -1]

# Part 1
num_numbers = len(rmem)
p1_sum = 0
rindex = 0
for i in range(num_numbers):
    n = mem[i]
    if n == -1:
        p1_sum += rmem[rindex] * i
        rindex += 1
    else:
        p1_sum += n*i
print(f"Part 1: {p1_sum}")

# Part 2
print("Part 2 is implemented in a bad way, takes 1 minute to complete..")
done = False
while not done:
    for i in range(len(p2_type)-1,-1,-1):
        if p2_type[i][2]: # Already visited or empty
            continue 
        p2_type[i][2] = True

        moved = False
        for j in range(len(p2_type)):
            if i <= j: 
                continue
            if p2_type[j][0] == -1 and p2_type[j][1] >= p2_type[i][1]:
                p2_type[j][1] -= p2_type[i][1]
                p2_type.insert(j, copy.deepcopy(p2_type[i]))
                p2_type[i+1][0] = -1
                p2_type[i+1][2] = True
                moved = True
                break
        if moved: break
    if i == 0: 
        done = True

# Calculate p2 score
index  = 0
p2_sum = 0
for p in p2_type:
    if p[0] == -1:
        index += p[1]
    else:
        for i in range(p[1]):
            p2_sum += p[0]*index
            index  += 1
print(f"Part 2: {p2_sum}")
