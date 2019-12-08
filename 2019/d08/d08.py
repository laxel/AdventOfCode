f = open("input.txt")
width = 25
height = 6

r = f.read()
r = r[:-1] # Remove last element (\n)
rows = [r[i * width:(i + 1) * width] for i in range((len(r) + width - 1) // width )]
layers = [rows[i * height:(i + 1) * height] for i in range((len(rows) + height - 1) // height )]

# --- Part 1 ---
numZeroLayer = [sum([row.count('0') for row in lay]) for lay in layers]
index = numZeroLayer.index(min(numZeroLayer))
num1 = sum([row.count('1') for row in layers[index]])
num2 = sum([row.count('2') for row in layers[index]])
p1 = num1*num2
print("Part 1:",p1)

# --- part 2 ---
image = [[2 for _ in range(0,width)] for _ in range(0,height)]
for lay in layers:
	for y in range(0,height):
		for x in range(0,width):
			if image[y][x] == 2:
				image[y][x] = int(lay[y][x])
			
image = [''.join([('#' if c != 0 else ' ') for c in row]) for row in image]		
print("part 2:")	
[print(row) for row in image]
