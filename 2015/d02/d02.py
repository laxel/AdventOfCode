f = open("input.txt")

totWrapping = 0
totRibbon = 0

for line in f:
	dims = [int(x) for x in line.split('x')]
	dims.sort()
	# Wrapping
	slack = dims[0]*dims[1]
	totWrapping += 2*(dims[0]*dims[1]+dims[0]*dims[2]+dims[1]*dims[2]) + slack
	#Ribbon
	totRibbon += 2*(dims[0]+dims[1])+dims[0]*dims[1]*dims[2]
	
print("Part 1: " + str(totWrapping))
print("Part 2: " + str(totRibbon))
