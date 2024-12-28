import time 
f = open("input.txt")

# Parse input
moves   = []
p1_grid  = []
p2_grid  = []
part    = 0
for l in f:
    if part == 0:
        if l == "\n":
            part = 1
        else:
            p1_grid += [[x for x in l if x != "\n"]]
            row = []
            for c in l:
                if l == "\n": continue
                if c == "#": row += ['#','#']
                if c == "O": row += ['[',']']
                if c == ".": row += ['.','.']
                if c == "@": row += ['@','.']
            p2_grid += [row]

    else: # Part 2
        moves += [x for x in l if x != "\n"]


def print_grid(grid):
    height = len(grid)
    width  = len(grid[0])
    for y in range(height):
        s = ""
        for x in range(width):
            s += grid[y][x]
        print(s)
    print("")

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def update_grid_p1(move, ps):
    d = ['>','v','<','^'].index(move)
    dx, dy = dirs[d]
    px, py = ps
    if p1_grid[py+dy][px+dx] == '.':
        p1_grid[py][px]       = "."
        p1_grid[py+dy][px+dx] = "@"
        ps = (px+dx, py+dy)
    elif p1_grid[py+dy][px+dx] == '#':
        # do nothing..
        pass
    else: # Object in the way, check if it is possible to move it
        cx, cy = (px+dx,py+dy)
        while True:
            cx, cy = (cx+dx,cy+dy)
            if p1_grid[cy][cx] == '.':
                p1_grid[cy][cx]       = "O"
                p1_grid[py][px]       = "."
                p1_grid[py+dy][px+dx] = "@"
                ps = (px+dx, py+dy)
                break
            elif p1_grid[cy][cx] == '#':
                break
    return ps

height = len(p1_grid)
width  = len(p1_grid[0])
player_pos = (0,0)
for y in range(height):
    for x in range(width): 
        if p1_grid[y][x] == '@':
            player_pos = (x,y)

# Interactive mode :)
# while True:
#     print_grid(p1_grid)
#     inp = input()
#     player_pos = update_grid_p1(inp, player_pos)

for m in moves:
    player_pos = update_grid_p1(m,player_pos)
# Get score
p1_sum = 0
for y in range(height):
    for x in range(width): 
        if p1_grid[y][x] == 'O':
            p1_sum += y*100+x
print(f"Part 1: {p1_sum}")

# PART 2

def update_grid_p2(move, ps):
    d = ['>','v','<','^'].index(move)
    dx, dy = dirs[d]
    px, py = ps
    if p2_grid[py+dy][px+dx] == '.':
        p2_grid[py][px]       = "."
        p2_grid[py+dy][px+dx] = "@"
        ps = (px+dx, py+dy)
    elif p2_grid[py+dy][px+dx] == '#':
        # do nothing..
        pass
    else: # Object in the way, check if it is possible to move it
        # Logic for <,> and ^,v now behaves slightly differently, have two different cases for them
        if d == 0 or d == 2:
            # HORIZONTAL PUSH
            cx, cy = (px+dx,py+dy)
            check_list = [(px,py)]
            while True:
                cx, cy = (cx+dx,cy+dy)
                if p2_grid[cy][cx] == '.':
                    for x in range(cx,px,-dx):
                        p2_grid[cy][x] = p2_grid[cy][x-dx]
                    p2_grid[py][px]       = "."
                    ps = (px+dx, py+dy)
                    break
                elif p2_grid[cy][cx] == '#':
                    break
        else:
            # VERTICAL PUSH
            index = 0
            check_list = [ps]
            can_push = True
            while index < len(check_list):
                cx, cy = check_list[index]
                index += 1
                if p2_grid[cy+dy][cx] == "[":
                    if (cx,  cy+dy) not in check_list: check_list.append((cx,  cy+dy))
                    if (cx+1,cy+dy) not in check_list: check_list.append((cx+1,cy+dy))
                elif p2_grid[cy+dy][cx] == "]":
                    if (cx,  cy+dy) not in check_list: check_list.append((cx,  cy+dy))
                    if (cx-1,cy+dy) not in check_list: check_list.append((cx-1,cy+dy))
                elif p2_grid[cy+dy][cx] == "#":
                    can_push = False
                    break
            if can_push:
                ps = (px+dx, py+dy)
                for i in range(len(check_list)-1,-1,-1):
                    cx,cy = check_list[i]
                    p2_grid[cy+dy][cx] = p2_grid[cy][cx]
                    p2_grid[cy][cx] = '.'
    return ps


height = len(p2_grid)
width  = len(p2_grid[0])
player_pos = (0,0)
for y in range(height):
    for x in range(width): 
        if p2_grid[y][x] == '@':
            player_pos = (x,y)

# Interactive mode :)
# while True:
#     print_grid(p2_grid)
#     inp = input()
#     player_pos = update_grid_p2(inp,player_pos)

for m in moves:
    player_pos = update_grid_p2(m,player_pos)

# Get score
p2_sum = 0
for y in range(height):
    for x in range(width): 
        if p2_grid[y][x] == '[':
            p2_sum += 100*y+x
print(f"Part 2: {p2_sum}")