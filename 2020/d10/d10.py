f = open("input.txt")

outlets = []
for l in f:
    outlets.append(int(l))

outlets.sort()

# --- Part 1 --- 
res = [0,0,1] # Create list and count last value
res[outlets[0] - 1] += 1 # Add first value
for i in range(1, len(outlets)):
    r = outlets[i] - outlets[i-1]
    res[r-1] += 1

print("/P1/ 1d * 3d is: " + str(res[0 * res[2]]))

# 1, 3, 2, 1, 2, 1, 1, 1, 1

# 4, X, X, 7, 8
# 4, X, 6, X, 8
# 4, X, 6, 7, 8
# 4, 5, X, X, 8
# 4, 5, X, 7, 8
# 4, 5, 6, X, 8
# 4, 5, 6, 7, 8


# ---
# 1, 3, 4, 5, 6
# 2, 3, 2, 1, 1

# 1, X, 4, X, 6
# 1, X, 4, 5, 6

# ---
# 1, 3, 4, 6, 9
# 2, 2, 1, 1, 0

# 1, X, 4, 6, 9
# 1, 3, X, 6, 9
# 1, 3, 4, 6, 9


# --- Part 2 ---
diffs = [0] * len(outlets)
for i in range(len(outlets)):
    numWays = 0
    for d in range(1, 4):
        if i + d >= len(outlets):
            break
        numWays += 1 if outlets[i + d] - outlets[i] <= 3 else 0
    diffs[i] = numWays

prevNum = 1
totalComb = 1
for num in diffs:
    if num == 3:
        if prevNum == 1:
            totalComb *= 4
        elif prevNum == 2:
            totalComb *= 4
        elif prevNum == 3:
            totalComb *= 7/4
    elif num == 2:
        if prevNum == 1:
            totalComb *= 2
        elif prevNum == 2:
            totalComb *= 3/2
        elif prevNum == 3:
            totalComb *= 1
    prevNum = num
            
print(totalComb)
print(outlets)
print(diffs)
