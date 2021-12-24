f = open("input.txt")
nums = [x.split('\n')[0] for x in f]

def bin_to_dec(binary_number):
    return sum([b * 2**exp for exp,b in zip(reversed(range(0,len(binary_number))), binary_number)])

num_entries = len(nums)

# Part 1
occ = [0]*len(nums[0])
for n in nums:
    ln = [c for c in n]
    occ = [int(a)+int(b) for a,b in zip(occ,ln)]

gamma = [1 if x > (num_entries/2) else 0 for x in occ]
eps   = [0 if x > (num_entries/2) else 1 for x in occ]

dec_gamma = bin_to_dec(gamma)
dec_eps   = bin_to_dec(eps)
p1 = dec_gamma * dec_eps

print("Part 1: {}(gamma) * {}(eps) = {}".format( dec_gamma, dec_eps, p1))

# Part 2
def p2_rating(l, majority_number):
    i = 0
    curr_list = l
    while len(curr_list) > 1: 
        num_entries = len(curr_list)
        indexed_list = [x[i] for x in curr_list]   

        if majority_number == '1':
            majority = 1 if indexed_list.count('1') >= num_entries/2 else 0
        elif majority_number == '0':
            majority = 0 if indexed_list.count('1') > num_entries/2 else 1
            majority = 0 if indexed_list.count('1') == num_entries/2 else majority
        
        
        curr_list = [l for il, l in zip(indexed_list, curr_list) if int(il) == majority]
        i += 1

    return [int(x) for x in curr_list[0]]

oxygen_rating = bin_to_dec(p2_rating(nums, '1'))
CO2_rating    = bin_to_dec(p2_rating(nums, '0'))

p2 = oxygen_rating * CO2_rating
print("Part 2: {}(oxygen) * {}(C02) = {}".format(oxygen_rating, CO2_rating, p2))