f = open("input.txt")


houses = {}
houses[(0,0)] = 1
totHouses = 1

def santa(instr):
	global totHouses
	x = 0
	y = 0

	for c in instr:
		if c == '<':
			x -= 1
		elif c == '>':
			x += 1
		elif c == 'v':
			y -= 1
		elif c == '^':
			y += 1
			
		if (x,y) in houses:
			houses[(x,y)] += 1
		else:
			houses[(x,y)] = 1
			totHouses += 1


string = f.read()

santa(string)
print("Part 1:",totHouses)

houses = {}
totHouses = 1
santa(string[::2])
santa(string[1:][::2])
print("Part 2:",totHouses)
