from functools import reduce

rawInput = open("input.txt").read().splitlines()
# Parse the raw input by removing tabs and converting from string to int.
input = [[int(y) for y in group] for group in [x.split("\t") for x in rawInput]] 

# Part 1
sum = 0
for l in input: 
    sum += max(l) - min(l)
print("Part1: " + str(sum))

# Part 2
sum = 0
for l in input:
    for i in range(0, len(l)): 
        div = l[i]
        bList = [(i % div == 0 if i != div else False) for i in l]
        result = reduce((lambda a,b: a or b), bList)
        if result:
            index = bList.index(True)
            sum += l[index] / div
print("Part2: " + str(int(sum)))
