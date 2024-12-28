f = open("input.txt")

# Create grid with "." padding in every direction 
grid = []
for l in f:
    grid.append(["."]+[c for c in l if c != "\n"]+["."])
padding = ["."]*len(grid[0])
grid.insert(0, padding)
grid += [padding]
width  = len(grid[0])
height = len(grid)

d = [(1,0), (0,1), (-1,0), (0,-1)]
def get_field_values_n_replace(x,y):
    a, p, s = (0, 0, 0)
    c = grid[y][x]
    visited = []
    side_halo = []
    queue = [(x,y)]
    # Calculate area, perimiter, and "side halo"
    while len(queue) != 0:
        qx, qy = queue.pop(0)
        if (qx,qy) in visited: continue
        visited.append((qx,qy))
        
        for i in range(len(d)):
            dx, dy = d[i]
            if grid[qy+dy][qx+dx] == c:
                queue.append((qx+dx,qy+dy))
            elif (qx+dx,qy+dy) not in visited:
                p += 1
                if (qx+dx,qy+dy) not in side_halo:
                    side_halo += [(qx+dx,qy+dy)]
        a += 1
        grid[qy][qx] = "-"
    # Calculate number of sides using "side halo" and turtles
    # The side halo have highlighted all coordinates that are neighboring to the 
    # field we are currently looking at. A turtle is then deployed to walk around 
    # the shape and go over all the halo squares.
    while len(side_halo) != 0:
        tx,ty = side_halo.pop(0)
        td    = 0
        # Calculate turtle starting direction
        for i in range(len(d)):
            dx, dy = d[i]
            if (tx+dx, ty+dy) in visited:
                td = (i-1) % 4
        # Start walk
        start_pos = (tx,ty,td)
        while True:
            # Move turtle
            # Check if it has field to the right of it. If not, turn right and go forward
            dx, dy = d[(td+1) % 4]
            if (tx+dx, ty+dy) not in visited:
                td = (td+1) % 4
                tx += dx 
                ty += dy
                s  += 1
            else:
                # Check if turtle has something in front of it. If it has, turn left
                dx, dy = d[td]
                if (tx+dx, ty+dy) in visited:
                    td = (td-1) % 4
                    s  += 1
                else: # Neither conditon is true, just go straight
                    tx += dx
                    ty += dy

            if (tx,ty) in side_halo:
                side_halo.remove((tx,ty))

            if (tx,ty,td) == start_pos: # Back to starting pos and direction, exit!
                break

    return (a,p,s)

def print_grid(tx,ty,d):
    for y in range(height):
        s = ""
        for x in range(width):
            if d != -1 and y == ty and x == tx:
                s += [">","v","<","^"][d]
            else:
                s += grid[y][x]
        print(s)

p1_sum = 0
p2_sum = 0
for y in range(1,height-1):
    for x in range(1,width-1):
        c = grid[y][x]
        if c == "-": continue
        a, p, s = get_field_values_n_replace(x,y)
        # print(f"Part1: A region of {c} plants with price {a}*{p}={a*p}.")
        # print(f"Part2: A region of {c} plants with price {a}*{s}={a*s}.")
        p1_sum += a*p
        p2_sum += a*s
print(f"Part 1: {p1_sum}")
print(f"Part 2: {p2_sum}")