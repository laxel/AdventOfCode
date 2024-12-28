import re

f = open("input.txt")
eqs = []
while True:
    A = f.readline()
    B = f.readline()
    P = f.readline()
    eqs += [[[int(x) for x in re.findall("\d+", A)], \
            [int(x) for x in re.findall("\d+", B)], \
            [int(x) for x in re.findall("\d+", P)]  \
            ]]
    E = f.readline()
    if E == '':
        break

# First tried to brute force solution. Worked for part 1 but not part 2...
# Just solved the equations instead and now it finishes in the blink of an eye :)

# Button A: X+ax, Y+ay
# Button B: X+bx, Y+by
# Prize: X=xr, Y=yr
# 1) ax*A+bx*B = xr
# 2) ay*A+by*B = yr
# Everything is known except for A and B
# From 1):
# A = (xr-bx*B)/ax
# From 2)
# B = (yr-ay*A)/by
# Combining both to get value of A:
# A                = (xr-bx*( (yr-ay*A)/by ))/ax
# A                = (xr - bx*yr/by + bx*ay*A/by)/ax
# ax*A             = xr - bx*yr/by + bx*ay*A/by
# A(ax - bx*ay/by) = xr - bx*yr/by
# A                = (xr - bx*yr/by) / (ax - bx*ay/by)

# In following example:
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# A = (8400 - 22*5400/67) / (94 - 22*34/67) = 80
# B = (5400-34*80)/67 = 40
# Correct!

psum = [0,0]
for eq in eqs:
    for p in range(2):
        ax, ay = eq[0]
        bx, by = eq[1]
        xr, yr = eq[2]
        if p == 1:
            xr += 10000000000000
            yr += 10000000000000
        A = (xr - bx*yr/by) / (ax - bx*ay/by)
        B = (yr-ay*A)/by
        # To fix some floating point errors, take the rounded value of
        # A and B and dubbel check that it is actually the correct solution.
        Ar = round(A)
        Br = round(B)
        if Ar*ax+Br*bx == xr and Ar*ay+Br*by == yr:
            psum[p] += 3*Ar + 1*Br
for p in range(2):
    print(f"Part {p+1}: {psum[p]}")
