f = open("input.txt")

eqs = []
for l in f:
    ans,nums = l.split(":")
    eq = [int(ans), [int(x) for x in nums.split(" ") if x != '']]
    eqs.append(eq)
# Part 1
def is_set(x, n):
    return x & 1 << n != 0
p1_sum = 0
for eq in eqs:
    # Loop over all possible combinations
    for i in range(2**(len(eq[1])-1)):
        sum = eq[1][0]
        for j in range(1, len(eq[1])):
            if is_set(i,j-1):
                sum *= eq[1][j]
            else:
                sum += eq[1][j] 
        if sum == eq[0]:
            p1_sum += sum
            break
print(f"Part 1: {p1_sum}")
# Part 2
p2_sum = 0
for eq in eqs:
    # Loop over all possible combinations
    oplist = [0]*(len(eq[1])-1)
    nextexit = False
    while True:
        sum = eq[1][0]
        for i in range(len(oplist)):
            if oplist[i] == 0:
                sum += eq[1][i+1]
            elif oplist[i] == 1:
                sum *= eq[1][i+1]
            else:
                sum = int(str(sum)+str(eq[1][i+1]))
        if sum == eq[0]:
            p2_sum += sum
            break
        for i in range(len(oplist)):
            oplist[i] += 1
            if oplist[i] == 3:
                oplist[i] = 0
                if i == len(oplist)-1: 
                    nextexit = True 
            else:
                break
        if nextexit: 
            break
           
print(f"Part 2: {p2_sum}")
