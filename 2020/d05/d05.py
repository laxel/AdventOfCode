import math

f = open("input.txt")

p2_list = []
highest = 0
for l in f:
    order = [c for c in l if c != '\n']
    l_row, u_row = [0, 127]
    l_col, u_col = [0,7]
    # Calculate row
    for c in order[:-3]:
        if c == 'F':
            u_row -= math.ceil((u_row - l_row)/2)
        elif c == 'B':
            l_row += math.ceil((u_row - l_row)/2)
    # Calculate colum
    for c in order[-3:]:
        if c == 'L':
            u_col -= math.ceil((u_col - l_col)/2)
        elif c == 'R':
            l_col += math.ceil((u_col - l_col)/2)
    # Task 1
    seat_id = l_row * 8 + l_col
    if seat_id > highest:
        highest = seat_id
    # Task 2
    p2_list.append(seat_id)

print("/P1/ Highest seat id: " + str(highest))

p2_list.sort()
p_v = p2_list[0] - 1
for v in p2_list:
    if v != p_v + 1:
        print("/P2/ Missing seat id: " + str(p_v + 1))
        break
    p_v = v
 
