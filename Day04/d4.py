rawInput = open("input.txt").read().splitlines()
input = [s.split() for s in rawInput]

# --- Part 1 ----
def d4a(inp):
    numValid = 0
    for l in inp:
        valid = True
        for fst in range(len(l)):
            snd = fst + 1
            while snd < len(l):
                if l[fst] == l[snd]: valid = False
                snd += 1
        if valid == True: numValid += 1
    
    return numValid

print("Part 1: " + str(d4a(input)))

# --- Part 2 ---
sortedList = [[''.join(sorted(y)) for y in x] for x in input]
print("Part 2: " + str(d4a(sortedList)))