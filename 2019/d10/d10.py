from math import gcd, atan2, degrees, sqrt

# Parse input
f = open("input.txt")
asteroids = []
y = 0
for l in f:
	x = 0
	for c in l:
		if c == '#':
			asteroids.append([x,y]);
		x += 1
	y += 1
width = x - 2
height = y - 1

# --- Part 1 ---

maxSeen = 0
bestCoord = [-1,-1]

for currAst in asteroids:
	astRmCopy = asteroids.copy()
	for trgAst in asteroids:
		if currAst == trgAst:
			continue
		
		xDiff = trgAst[0] - currAst[0]
		yDiff = trgAst[1] - currAst[1]
		divider = gcd(xDiff,yDiff)
		xDiff /= divider
		yDiff /= divider
		[x,y] = trgAst
		x += xDiff
		y += yDiff
		while not(x < 0 or x > width or y < 0 or y > height):
			if [x,y] in astRmCopy:
				astRmCopy.remove([x,y])
			
			x += xDiff
			y += yDiff

	if len(astRmCopy) > maxSeen:
		bestCoord = currAst
		maxSeen = len(astRmCopy)

print("Part 1:", bestCoord, maxSeen-1)

# --- Part 2 ---

# Build dictonary of the degree to each asteroid
degDict = {}
[x0,y0] = bestCoord
for astr in asteroids:
	if astr == bestCoord: continue
	[x,y] = astr
	deg = degrees(atan2(y0-y,x-x0))
	deg = 90 - deg
	if deg < 0: deg += 360
	if deg in degDict:
		degDict[deg].append([x,y])
	else:
		degDict[deg] = [[x,y]]


sortedKeys = list(degDict.keys())
sortedKeys.sort()
numDestroyed = 0
p2 = None
while numDestroyed < len(asteroids)-1:
	for key in sortedKeys:
		l = degDict[key]
		if len(l)==0: continue
		closest = 100000 # Very high number
		closestCoord = None
		for ast in l:
			if sqrt((x0-x)**2+(y0-y)**2) < closest:
				closestCoord = ast
				closest = sqrt((x0-x)**2+(y0-y)**2)
		l.remove(ast)
		numDestroyed += 1
		if numDestroyed == 200:
			p2 = ast

print("Part 2:",p2[0]*100+p2[1])
		





