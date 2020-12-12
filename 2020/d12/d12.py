import math

f = open("input.txt")

def rotate(x,y,angle):
    s = int(math.sin(math.radians(angle)))
    c = int(math.cos(math.radians(angle)))
    xnew = x * c - y * s
    ynew = x * s + y * c
    return [xnew, ynew]

p1_x, p1_y = [0,0]
facing = 0
x_facing = [1, 0, -1, 0]
y_facing = [0, -1, 0, 1]

p2_x, p2_y = [0,0]
w_x, w_y = [10,1]

for l in f:
    cmd = l[:1]
    num = int(l[1:-1])
    if cmd == 'L':
        facing -= int(num/90)
        facing %= 4
        w_x, w_y = rotate(w_x,w_y,num)
    elif cmd == 'R':
        facing += int(num/90)
        facing %= 4
        w_x, w_y = rotate(w_x,w_y,-num)
    elif cmd == 'F':
        p1_x += x_facing[facing] * num
        p1_y += y_facing[facing] * num
        p2_x += w_x * num
        p2_y += w_y * num
    elif cmd == 'N':
        p1_y += num
        w_y += num
    elif cmd == 'S':
        p1_y -= num
        w_y -= num
    elif cmd == 'E':
        p1_x += num
        w_x += num
    elif cmd == 'W':
        p1_x -= num
        w_x -= num

p1_man_dist = abs(p1_x) + abs(p1_y)
p2_man_dist = abs(p2_x) + abs(p2_y)

print("/P1/ Manhattan distance: " + str(p1_man_dist) + " (coord " + str(p1_x) + ", " + str(p1_y) + ")")
print("/P1/ Manhattan distance: " + str(p2_man_dist) + " (coord " + str(p2_x) + ", " + str(p2_y) + ")")