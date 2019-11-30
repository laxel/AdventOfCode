# Part 1
rawInput = open("input.txt").read().splitlines()[0]
input = [int(s) for s in list(rawInput)]

sum = 0
prev = input[len(input) -1]

for i in input:   
    if i == prev:
        sum += i
    prev = i

print("Part1: " + str(sum))

# Part 2
jumpIndex = int(len(input) / 2)
n = input[jumpIndex]
sum = 0
for i in input:
    if i  == n:
        sum += i

    jumpIndex += 1
    if jumpIndex >= len(input): 
        jumpIndex = 0
    n = input[jumpIndex]

print("Part2: " + str(sum))