f = open("input.txt")

# Parse grid
grid = []
for l in f:
    grid.append([x for x in l if x != '\n'])
width  = len(grid[0])
height = len(grid)
# Search for start
cx, cy = (0,0)
dirr   = 0 # Direction: Up=0, Right=1, Down=2, Left=3
for y in range(height):
    for x in range(width):
        if grid[y][x] == '^':
            cx, cy = (x,y)
sx, sy = (cx, cy)

def get_coord(x,y,d):
    if d == 0:
        tx, ty = (x,y-1)
    elif d == 1:
        tx, ty = (x+1,y)
    elif d == 2:
        tx, ty = (x,y+1)
    else:
        tx, ty = (x-1,y)
    if tx < 0 or tx >= width or ty < 0 or ty >= height:
        return (True, (x,y))
    return (False, (tx,ty))

def print_grid():
    for y in range(height):
        s = ""
        for x in range(width):
            s += grid[y][x]
        print(s)
    
# Part 1
#   Just do the walk normally, mark spaces walked with X's
while True:
    grid[cy][cx] = 'X'
    oob, (tx, ty) = get_coord(cx, cy, dirr)
    if oob: break # Out of bounds check failed, exit!
    if grid[ty][tx] == "#":
        dirr = (dirr+1) % 4
    else:
        (cx,cy) = (tx,ty)
# Count number of Xs
p1_sum = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'X': p1_sum += 1
# print_grid()
print("Part 1: "+str(p1_sum))

# Part 2:
def do_walk_p2(ix,iy,id):
    visited = [[[0 for k in range(4)] for j in range(width)] for i in range(height)]
    while True:
        # Save current state in visited list
        visited[iy][ix][id] = True
        oob, (tx, ty) = get_coord(ix, iy, id)
        if oob: return False # Out of bounds check failed, no infinite loop found!
        if grid[ty][tx] == "#":
            id = (id+1) % 4
        else:
            (ix,iy) = (tx,ty)
        # Check if new position has been visited before
        if visited[iy][ix][id]:
            return True # Repeat found meaning infinit loop!

p2_sum = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'X' and (x,y) != (sx,sy):
            grid[y][x] = '#'
            if do_walk_p2(sx, sy, 0): p2_sum += 1
            grid[y][x] = 'X'
print("Part 2: "+str(p2_sum))