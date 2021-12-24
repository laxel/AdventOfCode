f = open("input.txt")
nums = [int(x) for x in f]

# Part 1
p1 = [a > b for a,b in zip(nums[1:],nums[:-1])].count(True)
print("Part 1: " + str(p1))

# Part 2
prev = None
p2 = 0
for i in range(0,len(nums)-2):
    val = sum(nums[i:i+3])
    if prev != None and prev < val:
        p2 += 1
    prev = val

print("Part 2: " + str(p2))