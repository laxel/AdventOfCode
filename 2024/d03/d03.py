import re
f = open("input.txt")

p1_sum = 0
p2_sum = 0
p2active = True
for l in f:
    matches = re.findall("(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))",l)
    for m in matches:
        if m[0] != '':
            p1_sum += int(m[1]) * int(m[2])
            if p2active:
                p2_sum += int(m[1]) * int(m[2])
        if m[3] != '':
            p2active = True
        if m[4] != '':
            p2active = False
                
print("Part 1: "+str(p1_sum))
print("Part 2: "+str(p2_sum))