import time

f = open("input.txt")
startList = [int(x) for x in f.read().split(",")]


def intCode(l, inp, i, relBase):
	output = []
	relativeBase = relBase # VERY UGLY CODE
	
	def setList(l, trdParam, value):
		if trdParam == 0:
			l = checkAndExpand(l, l[i+3])
			l[l[i+3]] = value
		elif trdParam == 2:
			l = checkAndExpand(l, l[i+3] + relativeBase)
			l[l[i+3] + relativeBase] = value
		return l
		
	while str(l[i])[-2:] != '99':
		s = str(l[i])
		opcode = (5-len(s))*'0'+s
		cmd = opcode[-2:]
		fstPMode = int(opcode[2])
		sndPMode = int(opcode[1])
		trdPMode = int(opcode[0])
		
		l = checkAndExpand(l, [l[i+1], i+1, l[i+1] + relativeBase][fstPMode])
		fstP = None
		if fstPMode == 0:
			fstP = l[l[i+1]]
		elif fstPMode == 1:
			fstP = l[i+1]
		elif fstPMode == 2:
			fstP = l[l[i+1] + relativeBase]
		
		# One param. commands
		if cmd in ('03','04','09'): 
			if cmd == '03': # input
				l = checkAndExpand(l, l[i+1])
				if fstPMode == 0:
					l[l[i+1]] = inp
				elif fstPMode == 2:
					l[l[i+1] + relativeBase] = inp
			elif cmd == '04': # output
				output.append(fstP)
				if len(output) == 2:
					return (output,i+2,l, relativeBase)
			elif cmd == '09': # Change rel. base
				relativeBase += fstP
			i += 2
					
		# Two param. commands
		else:
			l = checkAndExpand(l, [l[i+2], i+2, l[i+2] + relativeBase][sndPMode])
			sndP = None
			if sndPMode == 0:
				sndP = l[l[i+2]]
			elif sndPMode == 1:
				sndP = l[i+2]
			elif sndPMode == 2:
				sndP = l[l[i+2] + relativeBase]
			
			if cmd in ('01','02','07','08'):
				l = checkAndExpand(l, l[i+3])
			
			if cmd in ('01','02'): # add/mul
				l = setList(l, trdPMode, fstP+sndP if cmd == '01' else fstP*sndP)
				i += 4
		
			elif cmd == '05': # jump-if-true
				if fstP != 0: 
					i = sndP
				else:
					i += 3
			elif cmd == '06': # jump-if-false
				if fstP == 0: 
					i = sndP
				else:
					i += 3
			elif cmd == '07': # less than
				l = setList(l, trdPMode, 1 if fstP < sndP else 0)
				i += 4
			elif cmd == '08': # equals	
				l = setList(l, trdPMode, 1 if fstP == sndP else 0)
				i += 4
	return (None,-1,l, relativeBase)

def checkAndExpand(l, index):
	diff = index - len(l) + 1
	if diff > 0:
		l = l + [0]*(diff+5)
	return l

def paintDict(d, dirr, x0, y0):
	size = 100
	for y in range(int(-size/6),int(size/6)):
		s = ''
		for x in range(int(-size/2),int(size/2)):
			if x == x0 and y == y0:
				s+= ['^','>','v','<'][dirr]
				
			else:
				if (x,y) not in d or d[(x,y)] == 0:
					s += '.'
				else:
					s += '#'
			s+= ' '
		
		print(s)

prg = startList.copy()

# ------ Toggle this value for part 1 or 2 ------
p1 = False

i = 0
pDict = {}
inp = 0 if p1 == True else 1
relBase = 0

currDir = 0
x = 0
y = 0

counter = 0

while True:
	# Run program
	[output,i,l, relBase] = intCode(prg,inp,i,relBase)
	prg = l
	if output == None:
		break
	[paint, dirChange] = output
	# Paint logic
	pDict[(x,y)] = paint
	
	# Direction/Coord. logic
	currDir += 1 if dirChange == 1 else -1
	if currDir == -1: currDir = 3
	if currDir ==  4: currDir = 0
	
	x += [0,1,0,-1][currDir]
	y += [-1,0,1,0][currDir]
	
	# Calculate next input value
	if (x,y) not in pDict:
		inp = 0
	else:
		inp = pDict[(x,y)]
	
	# --- Fancy printer ---
	#print(chr(27) + "[2J") # Clear screen
	#print(output)
	#paintDict(pDict, currDir, x, y)
	#time.sleep(0.05)

if p1 == True:
	print("Part 1: ",len(pDict))
else:
	paintDict(pDict, 0, 0, 0)
