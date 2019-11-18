f = open("input.txt")

numNice = 0

# Part 1
for line in f:
	cond1 = len(''.join(x for x in line if x in ('a','e','i','o','u'))) >= 3
	cond2 = any([line[i] == line[i+1]  for i in range(0,len(line)-1)])
	cond3 = not any(x in line for x in ['ab','cd','pq','xy'])
	
	if cond1 and cond2 and cond3:
		numNice += 1
		
print("Part 1:",numNice)

f = open("input.txt")

# Part 2
numNice = 0
for line in f:
	cond1 = False
	cond2 = False
	
	groups = [line[i] + line[i+1] for i in range(0,len(line)-1)]
	for j in range(1,len(groups)):
		overlapList = groups[0:j-1] + groups[j+2:]
		if groups[j] in overlapList:
			cond1 = True
			break
	
	cond2 = any([line[i-1] == line[i+1] for i in range(1,len(line)-1)])
		
	if cond1 and cond2:
		numNice += 1
print(numNice)
