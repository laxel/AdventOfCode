rawInput = open("input.txt").read().split("\t")
input = [int(s) for s in rawInput]

def search(list, num):
    for x in list:
        if x == num: return True
    return False

def listToNum(numList):
    s = ''.join(map(str, numList))
    return s

def toDublicate(inp):
    seen = [listToNum(inp)]
    numSteps = 0
    stop = False

    while not stop:
        index = -1
        maxVal = -1
        # Find biggest value
        for i in range(len(inp)):
            if inp[i] > maxVal:
                maxVal = inp[i]
                index = i
        # Redistribute
        inp[index] = 0
        y = index + 1 
        while maxVal > 0:
            if y >= len(inp):
                y = 0
            inp[y] += 1
            y += 1
            maxVal -= 1
        # Check if same as old
        num = listToNum(inp)
        if search(seen, num): 
            stop = True
        seen.append(num)
        numSteps += 1
    return seen


part1 = toDublicate(input)
print("Part 1: " + str(len(part1)-1))

part2 = toDublicate(input)
print("Part 2: " + str(len(part2)-1))