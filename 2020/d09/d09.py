f = open("input.txt")

preamble = 25
nums = []
for l in f:
    nums.append((int(l)))

# Part 1
p1_number = 0
for i in range(preamble, len(nums)):
    is_correct = False
    for f in range(i - preamble, i):
        for s in range(f + 1, i):
            if nums[f] + nums[s] == nums[i]:
                is_correct = True
                break
        if is_correct:
            break
    if not is_correct:
        p1_number = nums[i]
        break

print("/P1/ Wrong number is: " + str(p1_number))

# Part 2
p2_result = 0
should_break = False
for i in range(len(nums)):
    sum = nums[i]
    smallest = sum
    largest = sum
    for j in range(i+1, len(nums)):
        new_num = nums[j]
        sum += new_num
        if new_num < smallest:
            smallest = new_num
        if new_num > largest:
            largest = new_num
        
        if sum == p1_number:
            should_break = True
            p2_result = smallest + largest

    if should_break:
        break

print("/P2/ Sum of first/last: " + str(p2_result))



