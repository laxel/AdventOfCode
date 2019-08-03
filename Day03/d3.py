import math

input = 361527

# --- PART 1 ---

# Calculate on what layer the input is on
pos = 1
sideLength = 1
fstDist = 0
while pos + sideLength*4-4 < input:
    pos = pos + sideLength*4-4
    sideLength += 2
    fstDist += 1

# Calculate on what offset on that layer the input is on
while pos + sideLength-1 <= input: 
    pos = pos + sideLength-1

sndDist = abs(pos+math.floor(sideLength/2) - input)

print("Part 1: " + str(fstDist+sndDist))

# --- PART 2 ---

def getValue(grid, x, y):
    sum = 0
    sum += grid[y][x+1]
    sum += grid[y][x-1]
    sum += grid[y+1][x]
    sum += grid[y-1][x]
    sum += grid[y+1][x+1]
    sum += grid[y-1][x-1]
    sum += grid[y+1][x-1]
    sum += grid[y-1][x+1]
    return sum

size = 100
grid = [[0] * size for _ in range(size)]
posX = math.floor(size/2)
posY = math.floor(size/2)

grid[posY][posX] = 1

currValue = 0
dist2go = 0

counter = 0
while currValue < input:
    diffX = 0 if counter == 1 or counter == 3 else (1 if counter == 0 else -1)
    diffY = 0 if counter == 0 or counter == 2 else (-1 if counter == 1 else 1)
    if counter == 0 or counter == 2: dist2go += 1

    for _ in range(dist2go):
        posX += diffX
        posY += diffY
        currValue = getValue(grid, posX, posY)
        if currValue > input: break
        grid[posY][posX] = currValue

    counter += 1
    if counter > 3: counter = 0

print("Part 2: " + str(currValue))