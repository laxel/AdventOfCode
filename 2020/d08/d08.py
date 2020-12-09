f = open("input.txt")

instr = []
for l in f:
    inp = l.split()
    instr.append(inp)

def run_code(l):
    acc = 0
    pointer = 0
    visited = set()
    while True:
        if pointer >= len(l) or pointer < 0:
            break
        i, v = l[pointer]

        # Check if already visited
        if pointer in visited:
            break

        if i == "acc":
            acc += int(v)
        elif  i == "jmp":
            pointer += int(v) - 1
        
        visited.add(pointer)
        pointer += 1

    return [acc, 1 if pointer == len(l) else 0]

# Part 1
p1_acc = run_code(instr)[0]
print("/P1/ Accumilator at end: " + str(p1_acc))

# Part 2
p2_acc = 0
for j in range(len(instr)):
    i, v = instr[j]
    c_instr = instr.copy()

    if i == 'nop':
        c_instr[j] = ['jmp', v]
        if int(v) == 0:
            continue
    elif i == 'jmp':
        c_instr[j] = ['nop', v]
    
    res, cond = run_code(c_instr)
    if cond:
        p2_acc = res
        break

print("/P2/ Accumilator at end: " + str(p2_acc))
