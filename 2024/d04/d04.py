f = open("input.txt")
cmap = []
for l in f:
    cmap.append([x for x in l if x != '\n'])

width = len(cmap[0])
height = len(cmap)

# PART 1
word_p_req = 3 # -MAS
p1_sum = [0]*8
for y in range(height):
    for x in range(width):
        if cmap[y][x] != 'X':
            continue
        # Horizontel left check
        if (x - word_p_req >= 0) and (cmap[y][x-3:x+1]) == ['S','A','M','X']: 
            p1_sum[0] += 1
        # Horizontel right check
        if (x + word_p_req < width) and (cmap[y][x:x+4]) == ['X','M','A','S']: 
            p1_sum[1] += 1
        # Vertical Up
        if (y - word_p_req >= 0) and [a[x] for a in cmap[y-3:y+1]] == ['S','A','M','X']: 
            p1_sum[2] += 1
        # Vertical down
        if (y + word_p_req < height) and [a[x] for a in cmap[y:y+4]] == ['X','M','A','S']: 
            p1_sum[3] += 1
        # Diagonal up-left
        if (x - word_p_req >= 0 and y - word_p_req >= 0) and ([b2[b1] for b1,b2 in list(zip(list(range(4)), [a[x-3:x+1] for a in cmap[y-3:y+1]]))]) == ['S','A','M','X']: 
            p1_sum[4] += 1
        # Diagonal up-right
        if (x + word_p_req < width and y - word_p_req >= 0) and ([b2[3-b1] for b1,b2 in list(zip(list(range(4)), [a[x:x+4] for a in cmap[y-3:y+1]]))]) == ['S','A','M','X']: 
            p1_sum[5] += 1
        # Diagonal down-left
        if (x - word_p_req >= 0 and y + word_p_req < height) and ([b2[3-b1] for b1,b2 in list(zip(list(range(4)), [a[x-3:x+1] for a in cmap[y:y+4]]))]) == ['X','M','A','S']: 
            p1_sum[6] += 1
        # Diagonal down-right
        if (x + word_p_req < width and y + word_p_req < height) and ([b2[b1] for b1,b2 in list(zip(list(range(4)), [a[x:x+4] for a in cmap[y:y+4]]))]) == ['X','M','A','S']: 
            p1_sum[7] += 1

print("Part 1: "+str(sum(p1_sum)))

# PART 2
p2_sum = 0
for y in range(height):
    strr = ""
    for x in range(width):
        if cmap[y][x] != 'A' or (x < 1) or (width-x <= 1) or (y < 1) or (height-y <= 1):
            continue
        if ((cmap[y-1][x-1] == 'M' and cmap[y+1][x+1] == 'S') or (cmap[y-1][x-1] == 'S' and cmap[y+1][x+1] == 'M')) and \
           ((cmap[y-1][x+1] == 'M' and cmap[y+1][x-1] == 'S') or (cmap[y-1][x+1] == 'S' and cmap[y+1][x-1] == 'M')):
            p2_sum += 1

print("Part 2: "+str(p2_sum))
