rawInput = open("input.txt").read().splitlines()
input = [int(s) for s in rawInput]

# --- Part 1 ---
pos = 0
numSteps = 0
inp = input.copy()
while pos > -1 and pos < len(inp):
    inp[pos] += 1
    pos += inp[pos]-1
    numSteps += 1 

print("Part 1: " + str(numSteps))

# --- Part 2 ---
pos = 0
numSteps = 0
inp = input.copy()
while pos > -1 and pos < len(inp):
    temp = pos
    pos += inp[pos]
    inp[temp] += -1 if inp[temp] >= 3 else 1
    numSteps += 1 

print("Part 2: " + str(numSteps))