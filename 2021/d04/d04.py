f = open("input.txt")
lines = [x for x in f]

callNumbers = [int(x) for x in lines[0].split(",")]

boardsNums = []
boardsDone = []

# Intiate board data structure
for boardIndex in range(0,int((len(lines)-1)/6)):
    boardLines = lines[2 + boardIndex*6:2 + boardIndex*6 + 5]
    board = [[int(c) for c in l.split(" ") if c != ''] for l in boardLines]
    boardFlat = [n for line in board for n in line]
    boardsNums.append(boardFlat)
    boardsDone.append([False]*25)

firstBingo = True # Used by P1
boardsWithBingo = [False] * len(boardsNums) # Used by P2
# Loop through all numbers
for num in callNumbers:
	if all(boardsWithBingo):
		break
	# Check each board
	for boardIndex in range(0,len(boardsNums)):
		boardN = boardsNums[boardIndex]
		boardD = boardsDone[boardIndex]
		if num in boardN:
			index = boardN.index(num)
			boardD[index] = True
		# Check if Bingo
		horizontal = any([all(boardD[i:i+5]) for i in range(0,len(boardD),5)])
		vertical   = any([all(boardD[i::5]) for i in range(0,5)])
		if horizontal or vertical:
			# Bingo!
			if firstBingo:
				sumUnmarked = sum([n for n,c in zip(boardN,boardD) if not c])
				p1 = sumUnmarked * num
				print("Part 1: {} * {} = {}".format(sumUnmarked, num, p1))
				firstBingo = False
				continue
			
			boardsWithBingo[boardIndex] = True
			if all(boardsWithBingo):
				sumUnmarked = sum([n for n,c in zip(boardN,boardD) if not c])
				p2 = sumUnmarked * num
				print("Part 2: {} * {} = {}".format(sumUnmarked, num, p2))
				firstBingo = False
				break