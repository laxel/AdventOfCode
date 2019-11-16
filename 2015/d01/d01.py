f = open("input.txt")
s = f.read()
floor = 0
charAt = 1
fstBasement = -1
basementHit = False
for c in s:
	if c == ')':
		floor -= 1
	else:
		floor += 1
	
	if floor == -1 and basementHit == False:
		basementHit = True
		fstBasement = charAt
	charAt += 1

print("Part 1: " + str(floor))
print("Part 2: " + str(fstBasement))
