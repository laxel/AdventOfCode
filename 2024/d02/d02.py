f = open("input.txt")

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def calc_safe(int_list):
    pdiff = 0
    for i in range(1, len(int_list)):
        diff = int_list[i-1]-int_list[i]
        if (abs(diff) > 3) or (diff == 0) or (diff*pdiff < 0):
            return False
        pdiff = diff
    return True

p1_safe = 0
p2_safe = 0
for l in f:
    intl = [int(x) for x in l.split(" ")]
    # Part 1
    if calc_safe(intl):
        p1_safe += 1
        p2_safe += 1
        continue
    # Part 2 - Just brute force it yo
    for k in range(len(intl)):
        if calc_safe(intl[:k]+intl[k+1:]):
            p2_safe += 1
            break
    
print("Part 1: "+str(p1_safe))
print("Part 2: "+str(p2_safe))