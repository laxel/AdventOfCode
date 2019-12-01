import math

f = open("input.txt")

p1 = 0
p2 = 0
for l in f:
	p1 += math.floor(int(l)/3)-2
	f = int(l)
	while True:
		f = math.floor(f/3)-2
		if f <= 0: break
		p2 += f

print("Part 1: " + str(int(p1)))
print("Part 2: " + str(int(p2)))

