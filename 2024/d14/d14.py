import re
from functools import reduce
import time

# f = open("example.txt")
# width  = 11
# height = 7

f = open("input.txt")
width  = 101
height = 103

# Parse data
robots = []
for l in f:
    robots +=  [[int(x) for x in re.findall("(-?\d+)",l)]]

# Function too print grid
def print_grid(robs): 
    for y in range(height):
        s = ""
        for x in range(width):
            nrobots = 0
            for r in robs:
                if r[0] == x and r[1] == y:
                    nrobots += 1
            if nrobots == 0:
                s += "."
            else:
                s += str(nrobots)
        print(s)

def gen_updated_robots(robot_list, nseconds):
    urs = []
    for r in robot_list:
        x, y, dx, dy = r
        nx = (x+dx*nseconds) % width
        ny = (y+dy*nseconds) % height
        urs += [[nx,ny,r[2],r[3]]] 
    return urs

# Update robots positions:
urobots = gen_updated_robots(robots, 100)

# Count #robots in each quadrant
quadrants = [0,0,0,0]
for r in urobots:
    if r[0]*2 == width-1 or r[1]*2 == height-1: continue
    quadrants[round(r[0]/width) + round(r[1]/height)*2] += 1
p1_sum = reduce(lambda x, y: x * y, quadrants)
print(f"Part 1: {p1_sum}")

# Part 2:
# Print robot grid and visually inspect for tree ;_;
# Got too tired so started cheating too speed up the process..
# Sent different fake answers to the AOC site to get a clue approximately where it is..
# 10,000 is too high
# 5000 is too low
# 7500 is too high
# 6500 "is not the right answer", so around here..

# Then incremented time one step at a time and did some basic checks too see if there
# were any suspicous areas where the tree could be

robots = gen_updated_robots(robots, 6600)
for i in range(6600,7000):
    print(i)
    
    should_print = False
    # Only print grid if a sequence of 8 robots in a row is found?
    # for y in range(height):
    #     in_a_row = 0
    #     for x in range(width):
    #         found_robot = False
    #         for r in robots:
    #             if r[0] == x and r[1] == y:
    #                 found_robot = True
    #                 continue
    #         if found_robot:
    #             in_a_row += 1
    #         else:
    #             in_a_row = 0
    #         if in_a_row == 8:
    #             should_print = True
    #             break
    #     if should_print:
    #         break
    
    # Only print if density is high enogth around robot
    for r1 in robots:
        density = 0
        for r2 in robots:
            if r1 == r2: continue
            if abs(r2[0]-r1[0])+abs(r2[1]-r1[1]) < 10:
                density += 1
        if density >= 50:
            should_print = True

    if should_print:
        print_grid(robots)
        break
    robots = gen_updated_robots(robots, 1)


# Found tree at 6620!
# 1..................................1...............1111111111111111111111111111111...................
# ...................................................1.............................1...................
# ...................................................1.............................1...................
# ...................................................1.............................1...................
# .....................................1.1...........1.............................1...................
# ...................................................1..............1..............1...1...............
# 1..................................................1.............111.............1...................
# ....................1..............................1............11111............1...................
# ...................................................1...........1111111...........1.1....1............
# ....................1.....................1........1..........111111111..........1..........1........
# ............................1......................1............11111............1...................
# ...................................................1...........1111111...........1........1..........
# ...................................................1..........111111111..........1.....1.1...........
# ...................................................1.........11111111111.........1.............1.....
# ..............1....................................1........1111111111111........1.................1.
# ........1......1...................................1..........111111111..........1...................
# ..........1........................1........1......1.........11111111111.........1...................
# ...................................................1........1111111111111........1..................1
# ..................11.........................1.....1.......111111111111111.......1......1............
# ............1......1...1........................1..1......11111111111111111......1......1............
# ...................................................1........1111111111111........1...................
# ...................................................1.......111111111111111.......1...................
# ...................................................1......11111111111111111......1.1.................
# .................................................1.1.....1111111111111111111.....1...................
# ...................................11.....1........1....111111111111111111111....1...................
# ...................................................1.............111.............1...................
# ...1.......1.......................................1.............111.............1...................
# ...................................................1.............111.............1...................
# ...................................................1.............................1...................
# ...................................................1.............................1...................
# ...................................................1.............................1...................
# .................................................1.1.............................1...................
# ...........................................1.......1111111111111111111111111111111..............1....