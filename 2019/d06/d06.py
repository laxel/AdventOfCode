f = open("input.txt")
parentDict = {}

# Create tree dictunary
for l in f:
	temp = l.split(')')
	frm  = temp[0]
	to   = temp[1].split('\n')[0]
	parentDict[to] = frm

# --- Part 1 ---
p1 = 0
for k in parentDict:
	parent = k
	while parent != 'COM':
		parent = parentDict[parent]
		p1 += 1
print("Part 1:",p1)

# --- Part 2 ---
def parentList(word):
	parent = parentDict[word]
	l = [parent]
	while parent != 'COM':
		parent = parentDict[parent]
		l.append(parent)
	return l

youList = parentList('YOU')
sanList = parentList('SAN')
for p in youList:
	if p in sanList:
		numTransfers = youList.index(p) + sanList.index(p)
		print("Part 2:",numTransfers)
		break













