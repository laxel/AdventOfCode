inp_s = "14,1,17,0,3,20"
inp = [int(x) for x in inp_s.split(',')]

d = dict()
for t in range(len(inp) - 1):
    d[inp[t]] = t+1

p = inp[len(inp) - 1]
n = 0
for t in range(len(inp)+1, 30000001):
    if p in d:
        n = (t - 1) - d[p]
    else:
        n = 0
    d[p] = t - 1
    p = n
    if t == 2020:
        print("/P1/ 2020th number: " + str(p))
        print("P2 will take ≈ 1min")
    if t == 30000000:
        print("/P2/ 30000000th number: " + str(p))
