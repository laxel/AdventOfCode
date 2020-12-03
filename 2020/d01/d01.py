f = open("input.txt")

nums = []
for l in f:
    nums.append(int(l))

for a in range(0, len(nums)):
    for b in range(a+1, len(nums)):
        if nums[a] + nums[b] == 2020: 
            print("Right values was found at: (" + str(a) + ", " + str(b) + ") = (" + str(nums[a]) + ", " +str(nums[b]) +")" )
            print("Result 1: " + str(nums[a] * nums[b]))

        for c in range(b+1, len(nums)):
            if nums[a] + nums[b] + nums[c] == 2020:
                print("Right values was found at: (" + str(a) + ", " + str(b) + ", " + str(c) + ") = (" + str(nums[a]) + ", " +str(nums[b]) + ", " +str(nums[c]) +")" )
                print("Result 2: " + str(nums[a] * nums[b] * nums[c]))
            
            