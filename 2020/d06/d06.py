f = open("input.txt")

p1_s = set()
p1_sum = 0
p2_s = set()
p2_sum = 0
nextNew = True
for l in f:
    # Part 1
    if l == "\n":
        p1_sum += len(p1_s)
        p1_s = set()
    [p1_s.add(c) for c in l if c != "\n"]

    # Part 2
    if nextNew:
        [p2_s.add(c) for c in l if c != "\n"]
        nextNew = False
    elif l == "\n":
        p2_sum += len(p2_s)
        p2_s = set()
        nextNew = True
    else:
        checkAnsw = [c for c in l if c != "\n"]
        [p2_s.remove(x) for x in p2_s.copy() if not x in checkAnsw]

if len(p1_s) != 0: 
    p1_sum += len(p1_s)
if len(p2_s) != 0: 
    p2_sum += len(p2_s)

print("/P1/ Sum of answers: " + str(p1_sum))
print("/P2/ Sum of answers: " + str(p2_sum))

