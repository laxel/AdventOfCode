import re
from copy import deepcopy

f = open("input.txt")
moons = []
steps = 1000

# Parse input
for l in f:
	coords = re.findall("-?\d+", l)
	moons.append([[int(x) for x in coords],[0,0,0]])
p1Moons = deepcopy(moons)
p2Moons = deepcopy(moons)
# --- Part 1 ---

# Caluclate moon change
for _ in range(0,steps):
	# Calculate new velocity
	for i in range(0,len(p1Moons)):
		crM = p1Moons[i]
		for j in range(0,len(p1Moons)):
			ckM = p1Moons[j]
			if i != j:
				crM[1][0] += 0 if crM[0][0] == ckM[0][0] else 1 if crM[0][0] < ckM[0][0] else -1
				crM[1][1] += 0 if crM[0][1] == ckM[0][1] else 1 if crM[0][1] < ckM[0][1] else -1
				crM[1][2] += 0 if crM[0][2] == ckM[0][2] else 1 if crM[0][2] < ckM[0][2] else -1
	# Calculate new coords
	for m in p1Moons:
		m[0][0] += m[1][0]
		m[0][1] += m[1][1]
		m[0][2] += m[1][2]

# Get total energy
s = 0
for m in p1Moons:
	s += sum([abs(x) for x in m[0]]) * sum([abs(x) for x in m[1]])
print("Part 1:",s)


	
# --- Part 2 ---
prevPositions = set()
k = 0
# Caluclate moon change
while True:
	# Add and check set
	coords = tuple([tuple(x[0]) for x in p2Moons])
	#if ((-1, -8, 8), (2, 5, -1), (4, 0, 2), (3, -10, -7)) == coords:
		#print("At:",k)
	
	if coords in prevPositions:
		#print(k)
		#print("Copy:",coords)
		break
	prevPositions.add(coords)
	k += 1
	# Calculate new velocity
	for i in range(0,len(p2Moons)):
		crM = p2Moons[i]
		for j in range(0,len(p2Moons)):
			ckM = p2Moons[j]
			if i != j:
				crM[1][0] += 0 if crM[0][0] == ckM[0][0] else 1 if crM[0][0] < ckM[0][0] else -1
				crM[1][1] += 0 if crM[0][1] == ckM[0][1] else 1 if crM[0][1] < ckM[0][1] else -1
				crM[1][2] += 0 if crM[0][2] == ckM[0][2] else 1 if crM[0][2] < ckM[0][2] else -1
	# Calculate new coords
	for m in p2Moons:
		m[0][0] += m[1][0]
		m[0][1] += m[1][1]
		m[0][2] += m[1][2]

		

