import math

f = open("input.txt").readlines()
f = [x[:-1] for x in f] # Remove '\n'

# --- Part 1 ---
start = int(f[0])
lines = [int(l) for l in f[1].split(',') if l != 'x']

next_stop = [math.ceil(start/x) * x for x in lines]
closest_stop = min(next_stop)
closets_index = next_stop.index(closest_stop)
closest_dist = closest_stop - start
closest_id = lines[closets_index]

print("/P1/ Closest ID & dist: " + str(closest_id) + " * " + str(closest_dist) + " = " + str(closest_id * closest_dist))

# --- Part 2 ---
l = f[1].split(',')
s = int(l[0])
t = s
r = 1

for i in range(1, len(l)):
    c = l[i]
    if c == 'x':
        r += 1
    else:
        n = int(c)
        k = 1
        while True:
            if (t + r) % n == 0:
                break
            t += s
        s *= n
        r += 1

print("/P2/ First good time: " + str(t))