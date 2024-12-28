f = open("input.txt")

fdict = {}
y = -1
for l in f:
    x = -1
    y += 1
    for c in l:
        if c == '\n': continue
        x += 1
        if c == '.':  continue
        if c in fdict:
            fdict[c].append((x,y))
        else:
            fdict[c] = [(x,y)]
width  = x+1
height = y+1

p1_antinodes = []
p2_antinodes = []
for k in fdict:
    for i in range(len(fdict[k])):
        for j in range(len(fdict[k])):
            if i == j: continue
            a  = fdict[k][i]
            b  = fdict[k][j]
            dx = a[0]-b[0]
            dy = a[1]-b[1]
            # Part 1
            x = a[0]+dx
            y = a[1]+dy
            if not ((x < 0) or (x >= width) or (y < 0) or (y >= height)):
                if (x,y) not in p1_antinodes:
                    p1_antinodes.append((x,y))
            # Part 2
            x = a[0]
            y = a[1]
            while not ((x < 0) or (x >= width) or (y < 0) or (y >= height)):
                if (x,y) not in p2_antinodes:
                    p2_antinodes.append((x,y))
                x += dx
                y += dy
    
print(f"Part 1: {len(p1_antinodes)}")
print(f"Part 2: {len(p2_antinodes)}")

# print map
# for y in range(height):
#     s = ""
#     for x in range(width):
#         skip = False
#         for k in fdict:
#             if (x,y) in fdict[k]:
#                 s += k
#                 skip = True
#         if skip: continue
#         if (x,y) in p2_antinodes:
#             s += "#"
#         else:
#             s += '.'
#     print(s)