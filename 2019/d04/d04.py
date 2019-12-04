lower = 197487
upper = 673251

def adjCond1(inp):
	last = None
	for c in inp:
		if c == last:
			return True
		last = c
	return False

def adjCond2(inp):
	last = None
	sameInRow = 1
	for c in inp:
		if c == last:
			sameInRow += 1
		else:
			if sameInRow == 2:
				return True
			sameInRow = 1
		last = c
		
	if sameInRow == 2: return True
	return False
		
		

numPass1 = 0
numPass2 = 0
for n in range(lower,upper):
	s = str(n)
	if list(s) == sorted(s) and adjCond1(s):
		numPass1 += 1
	if list(s) == sorted(s) and adjCond2(s):
		numPass2 += 1
print("Part 1:", numPass1)	
print("Part 2:", numPass2)	

