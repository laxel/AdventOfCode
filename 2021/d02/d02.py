f = open("input.txt")
words = [x for x in f]

# Part 1
hori = 0
vert = 0
for l in words:
    cmd,num = l.split(" ")
    num = int(num)
    if cmd == "forward":
        vert += num
    else:
        hori += -num if cmd == "up" else num

p1 = vert * hori
print("Part 1: {} ({} * {})".format(p1, vert, hori))

# Part 2
hori, vert, aim = 0,0,0
for l in words:
    cmd,num = l.split(" ")
    num = int(num)
    if cmd == "forward":
        vert += num
        hori += aim*num
    else:
        aim += -num if cmd == "up" else num

p2 = vert * hori
print("Part 2: {} ({} * {})".format(p2, vert, hori))

