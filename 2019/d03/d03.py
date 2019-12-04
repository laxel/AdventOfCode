f = open("input.txt")

temp = f.read().split('\n')[:-1]
inp = [x.split(',') for x in temp]

def intersection(L1, L2):
	fstOr = "Ver" if L1[0][0]-L1[1][0] == 0 else "Hor"
	sndOr = "Ver" if L2[0][0]-L2[1][0] == 0 else "Hor"
	
	if fstOr == "Ver" and sndOr == "Hor":
		if (L1[0][0] > L2[0][0] and L1[0][0] < L2[1][0]) or (L1[0][0] < L2[0][0] and L1[0][0] > L2[1][0]):
			if (L2[0][1] > L1[0][1] and L2[0][1] < L1[1][1]) or (L2[0][1] < L1[0][1] and L2[0][1] > L1[1][1]):
				return (L1[0][0], L2[0][1])
				
			
	if fstOr == "Hor" and sndOr == "Ver":
		if (L2[0][0] > L1[0][0] and L2[0][0] < L1[1][0]) or (L2[0][0] < L1[0][0] and L2[0][0] > L1[1][0]):
			if (L1[0][1] > L2[0][1] and L1[0][1] < L2[1][1]) or (L1[0][1] < L2[0][1] and L1[0][1] > L2[1][1]):
				return (L2[0][0], L1[0][1])
					
	return None


pathList = []
for rawList in inp:
	lineList = []
	x = 0
	y = 0
	oldx = 0
	oldy = 0
	for rawDir in rawList:
		d = rawDir[0]
		i = int(rawDir[1:])
		x += (i if d == 'R' else -i) if (d in ('R','L')) else 0
		y += (i if d == 'U' else -i) if (d in ('U','D')) else 0
		lineList.append([[oldx,oldy],[x,y]])
		oldx = x
		oldy = y
	pathList.append(lineList)

intersectList = []
for line1 in pathList[0]:
	for line2 in pathList[1]:
		res = intersection(line1, line2)
		if res != None:
			intersectList.append(res)

closest = abs(intersectList[0][0])+abs(intersectList[0][1]) 
for p in intersectList:
	dist = abs(p[0])+abs(p[1])
	if dist < closest:
		closest = dist
		
print("Part 1:",closest)

intersectionDict = {}

for inter in intersectList:
	intersectionDict[inter] = 0

	

for rawList in inp:
	x = 0
	y = 0
	dist = 0
	for rawDir in rawList:
		d = rawDir[0]
		i = int(rawDir[1:])
		xadd = (i if d == 'R' else -i) if (d in ('R','L')) else 0
		yadd = (i if d == 'U' else -i) if (d in ('U','D')) else 0
		while xadd != 0 or yadd != 0:
			if (x,y) in intersectList:
				intersectionDict[(x,y)] += dist
			if xadd > 0:
				x += 1
				xadd -=1
			elif xadd < 0:
				x -= 1
				xadd +=1
			
			if yadd > 0:
				y += 1
				yadd -=1
			elif yadd < 0:
				y -= 1
				yadd +=1
			
			dist += 1
			

key_min = min(intersectionDict.keys(), key=(lambda k: intersectionDict[k]))

print("Part 2:",intersectionDict[key_min])
	
