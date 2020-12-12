import pprint

f = open("input.txt")

o_map = []
for l in f:
    o_map.append([c for c in l if c in ['.','L', '#']])
width = len(o_map[0])
height = len(o_map)

pp = pprint.PrettyPrinter(width=60, compact=False)

# Part 1 func
def check_adjacent(m,x,y):
    neighbours = 0
    for d_y in range(-1,2):
        for d_x in range(-1,2):
            if d_x == 0 and d_y == 0:
                continue
            if not 0 <= x + d_x < width:
                continue
            if not 0 <= y + d_y < height:
                continue
            if m[y + d_y][x + d_x] == '#':
                neighbours += 1
    return neighbours

# Part 1, main loop
occupied_seats = 0
has_changed = True
iteration = 0
r_map = [l.copy() for l in o_map]
while has_changed:
    has_changed = False
    occupied_seats = 0
    w_map = [l.copy() for l in r_map]
    for y in range(height):
        for x in range(width):
            if r_map[y][x] in ['L','#']:
                if r_map[y][x] == '#':
                    occupied_seats += 1
                
                num_neigh = check_adjacent(r_map,x,y)
                if r_map[y][x] == 'L' and num_neigh == 0:
                    w_map[y][x] = '#'
                    has_changed = True
                if r_map[y][x] == '#' and num_neigh >= 4:
                    w_map[y][x] = 'L'
                    has_changed = True
    r_map = [l.copy() for l in w_map]
    iteration += 1

print("/P1/ Num occupied seats: " + str(occupied_seats) + " (after " + str(iteration) + " iterations)")

# Part 2
def check_sight(m,x,y):
    d_x = [0,1,1,1,0,-1,-1,-1]
    d_y = [-1,-1,0,1,1,1,0,-1]
    num_see = 0
    for i in range(8):
        _x = x
        _y = y
        while True:
            _x += d_x[i]
            _y += d_y[i]
            if  not 0 <= _x < width or not 0 <= _y < height:
                break
            check = m[_y][_x]
            if check == 'L':
                break
            elif check == '#':
                num_see += 1
                break
    return num_see

occupied_seats = 0
has_changed = True
iteration = 0
r_map = [l.copy() for l in o_map]
while has_changed:
    has_changed = False
    occupied_seats = 0
    w_map = [l.copy() for l in r_map]
    for y in range(height):
        for x in range(width):
            check = r_map[y][x]
            if check != '.':
                if check == '#':
                    occupied_seats += 1
                
                num_neigh = check_sight(r_map,x,y)
                if check == 'L' and num_neigh == 0:
                    w_map[y][x] = '#'
                    has_changed = True
                if check == '#' and num_neigh >= 5:
                    w_map[y][x] = 'L'
                    has_changed = True
    r_map = [l.copy() for l in w_map]
    iteration += 1

print("/P2/ Num occupied seats: " + str(occupied_seats) + " (after " + str(iteration) + " iterations)")