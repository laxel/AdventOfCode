f = open("input.txt")
data = [int(x) for x in f.readline().split(" ")]

length = 75+1
saved = [{} for _ in range(length)]

def calc_blink(cdepth, num):
        if cdepth == 0:
             return 1
        elif num in saved[cdepth]:
            return saved[cdepth][num]
        else:
            s = str(num)
            if num == 0:
                depth = calc_blink(cdepth-1, 1)
            elif len(s) % 2 == 0:
                depth = calc_blink(cdepth-1, int(s[:int(len(s)/2)])) + calc_blink(cdepth-1, int(s[int(len(s)/2):]))
            else:
                depth = calc_blink(cdepth-1,num*2024)
                
            if num not in saved[cdepth]:
                 saved[cdepth][num] = depth
            return depth
# PART 1
p1_sum = 0
for d in data:
     p1_sum += calc_blink(25, d)
print(f"Part 1: {p1_sum}")
# PART 2
p2_sum = 0
for d in data:
     p2_sum += calc_blink(75, d)
print(f"Part 2: {p2_sum}")
