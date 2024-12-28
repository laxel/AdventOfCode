f = open("input.txt")

# Construct trail map
tmap = []
for l in f:
    tmap.append([int(c) for c in l if c != '\n'])
width = len(tmap[0])
height = len(tmap)
# Find trailheads
trailheads = []
for y in range(height):
    for x in range(width):
        if tmap[y][x] == 0:
            trailheads += [[x,y,0]]
p1_sum = 0
p2_sum = 0
for s in trailheads:
    queue = [s]
    endpoints = []
    while len(queue) != 0: 
        x,y,n = queue[0]
        if n == 9:
            p2_sum += 1
            if (x,y) not in endpoints:
                endpoints += [(x,y)]
        else:
            # Search neighboring tiles and add to queue if possible
            if x-1 >= 0 and tmap[y][x-1] == n+1:     # Left
                queue.append([x-1,y,n+1]) 
            if x+1 < width and tmap[y][x+1] == n+1:  # Right
                queue.append([x+1,y,n+1]) 
            if y-1 >= 0 and tmap[y-1][x] == n+1:     # Up
                queue.append([x,y-1,n+1]) 
            if y+1 < height and tmap[y+1][x] == n+1: # Down
                queue.append([x,y+1,n+1]) 
        del queue[0]
    p1_sum += len(endpoints)

print(f"Part 1: {p1_sum}")
print(f"Part 2: {p2_sum}")