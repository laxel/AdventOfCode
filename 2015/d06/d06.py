import re

# Init variables
f = open("input.txt")

p1 = [[ 0 for i in range(1000) ] for j in range(1000) ]
p2 = [[ 0 for i in range(1000) ] for j in range(1000) ]


# Helper function
def modify(part,_list, mode, x1, y1, x2, y2):
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):
		
			if mode == "on":
				if part == 1:
					_list[y][x] = 1
				else:
					_list[y][x] += 1
					
			elif mode == "off":
				if part == 1:
					_list[y][x] = 0
				elif _list[y][x] > 0:
					_list[y][x] -= 1
				
			elif mode == "toggle":
				if part == 1:
					_list[y][x] = 1 - _list[y][x] 
				else:
					_list[y][x] += 2


# iterate through input
for inp in f:
	match = re.search("(on|off|toggle) (\d+),(\d+) \w+ (\d+),(\d+)",inp)
	if match:
		g = match.groups()
		modify(1, p1,g[0],int(g[1]),int(g[2]),int(g[3]),int(g[4]))
		modify(2, p2,g[0],int(g[1]),int(g[2]),int(g[3]),int(g[4]))
	else:
		print("Error, input wrong format:", inp)


# Results
print("Part 1:",sum([sum(x) for x in p1]))
print("Part 2:",sum([sum(x) for x in p2]))
