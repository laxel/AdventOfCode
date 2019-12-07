from itertools import permutations 

f = open("input.txt")
startList = [int(x) for x in f.read().split(",")]

def intCode(l,phaseSetting, fromPrev, i):
	inp = [phaseSetting, fromPrev]
	inpI = 0 if i == 0 else 1
	output = None
	while str(l[i])[-2:] != '99':
		s = str(l[i])
		opcode = (5-len(s))*'0'+s
		cmd = opcode[-2:]
		fstPMode = opcode[2]
		sndPMode = opcode[1]
		
		if cmd in ('03','04'):
			if cmd == '03': # input
				l[l[i+1]] = inp[inpI]
				inpI += 1
				i += 2
			elif cmd == '04': # output
				if fstPMode == '0':
					output = l[l[i+1]] 
					return (output,i+2)
				else:
					output = l[i+1] 
					return (output,i+2)
				i += 2
		else:
			fstP = l[l[i+1]] if fstPMode == '0' else l[i+1]
			sndP = l[l[i+2]] if sndPMode == '0' else l[i+2]
			
			if cmd in ('01','02'): # add/mul
				l[l[i+3]] = fstP+sndP if cmd == '01' else fstP*sndP
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
				l[l[i+3]] = 1 if fstP < sndP else 0
				i += 4
			elif cmd == '08': # equals	
				l[l[i+3]] = 1 if fstP == sndP else 0
				i += 4
	return (None,-1)
	
# --- Part 1 ---
everySeq = list(permutations([0, 1, 2, 3, 4]))
maxOutput = 0
for seq in everySeq:
	output = 0
	for s in seq:
		output = intCode(startList.copy(),s,output,0)[0]
	if output > maxOutput:
		maxOutput = output
print("Part 1:",maxOutput)

# --- Part 2 ---
everySeq = list(permutations([5,6,7,8,9]))
maxOutput = 0

for seq in everySeq:
	ampState = [[0,startList.copy()] for _ in range(0,5)]
	output = 0
	for i in range(0,len(ampState)):
		temp = intCode(ampState[i][1],seq[i],output,0)
		output = temp[0]
		ampState[i][0] = temp[1]
		
	realOutput = 0
	ampIndex = 0
	while ampState[len(ampState)-1][0] != -1:
		temp = intCode(ampState[ampIndex][1],None, output, ampState[ampIndex][0])
		output = temp[0]
		ampState[ampIndex][0] = temp[1]
		ampIndex += 1
		if output != None:
			realOutput = output
		if ampIndex == 5: 
			ampIndex = 0
	if realOutput > maxOutput:
		maxOutput = realOutput

print("Part 2:",maxOutput)
