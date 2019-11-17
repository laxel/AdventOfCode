import hashlib 

_input = "yzbqklnj"
i = 0
p1 = -1
p2 = -1
p1Done = False

while True:
	word = _input + str(i)
	result = hashlib.md5(word.encode()).hexdigest()
	if result[:5] == "00000" and p1Done == False:
		p1 = i
		p1Done = True
		
	if result[:6] == "000000":
		p2 = i
		break
		
	i += 1
print("Part 1:",p1)
print("Part 2:",p2)
