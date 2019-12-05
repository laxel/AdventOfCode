f = open("input.txt")
l = [int(x) for x in f.read().split(",")]

# Input 1 for part 1
# Input 5 for part 2
inp = 5

i = 0
while str(l[i])[-2:] != '99':
	s = str(l[i])
	opcode = (5-len(s))*'0'+s
	cmd = opcode[-2:]
	fstPMode = opcode[2]
	sndPMode = opcode[1]
	
	if cmd in ('03','04'):
		if cmd == '03': # input
			l[l[i+1]] = inp
			i += 2
		elif cmd == '04': # output
			if fstPMode == '0':
				print(i,l[l[i+1]])
			else:
				print(i,l[i+1]) 
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
	

	
	
		






