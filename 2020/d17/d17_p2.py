f = open("input.txt").readlines()

m = []

for y in range(len(f)):
    for x in range(len(f[y])):
        if f[y][x] == '#':
            m.append((x,y,0,0))
    y += 1

x_th = [0,int(len(f[0])) - 1]
y_th = [0,int(len(f[0])) - 1] 
z_th = [0,0]
w_th = [0,0]

def check_neigh(d,x,y,z,w):
    num_neigh = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                for dw in [-1,0,1]:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if (x + dx, y + dy, z + dz, w + dw) in d:
                        num_neigh += 1
    return num_neigh

def update_threashold(x,y,z,w):
    if x < x_th[0]:
        x_th[0] = x
    if x > x_th[1]:
        x_th[1] = x
    if y < y_th[0]:
        y_th[0] = y
    if y > y_th[1]:
        y_th[1] = y
    if z < z_th[0]:
        z_th[0] = z
    if z > z_th[1]:
        z_th[1] = z
    if w < w_th[0]:
        w_th[0] = w
    if w > w_th[1]:
        w_th[1] = w

def print_map(d):
    for z in range(z_th[0], z_th[1]+1):
        print("z="+str(z))
        for y in range(y_th[0], y_th[1]+1):
            for x in range(x_th[0], x_th[1]+1):
                if (x,y,z) in d:
                    print("#",end='')
                else:
                    print(".",end='')
            print("")
        print("")

for i in range(6):
    n_m = []
    for x in range(x_th[0] - 1, x_th[1] + 2):
        for y in range(y_th[0] - 1, y_th[1] + 2):
            for z in range(z_th[0] - 1, z_th[1] + 2):
                for w in range(w_th[0] - 1, w_th[1] + 2):   
                    nn = check_neigh(m,x,y,z,w)
                    if (x,y,z,w) in m:
                        if nn in [2,3]:
                            n_m.append((x,y,z,w))
                            update_threashold(x,y,z,w)
                    else: 
                        if nn == 3:
                            n_m.append((x,y,z,w))
                            update_threashold(x,y,z,w)
    m = n_m
   
    print("Iteration " + str(i+1) + " done, num cells active: " + str(len(m)))


    

                            
