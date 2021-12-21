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
				if len(output) == 3:
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

# --- Part 1 ---
l = startList.copy()
relBase = 0
i = 0

x = 0
oldY = 0
s = ''
blocks = 0

while True:
	[output, i, l, relBase] = intCode(l, 0,i, relBase)
	if output == None:
		break
	[x,y,block] = output
	if block == 2:
		blocks += 1	
print("Part 1:", blocks)

# --- Part 2 ---
l = startList.copy()
l[0] = 2
relBase = 0
i = 0
score = 0

x = 0
oldY = 0
s = ''

while True:
	[output, i, l, relBase] = intCode(l, 0,i, relBase)
	print(output)
	if output == None:
		break
	[x,y,block] = output
	
	if x == -1 and y == 0:
		score = blocks
	else:
		if oldY != y:
			oldY = y
			print(s)
			s = ''	
		s += ['.', '#', 'B', 'P', 'b'][block]
		s += '.'	
print(blocks)











