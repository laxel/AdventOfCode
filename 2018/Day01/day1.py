# Part 1
file = open("input.txt")
l = file.readlines()

sum = 0
for line in l:
    sum += int(line)

print("Part 1: " + str(sum))

# Part 2
currFreq = 0
s = {0}
i = 0

while True:
    if i >= len(l):
        i = 0

    currFreq += int(l[i])

    if {currFreq}.issubset(s):
        print("Part 2: " + str(currFreq))
        break
    s.add(currFreq)

    i += 1